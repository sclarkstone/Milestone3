import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug import utils
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


def is_logged_in():
  if session and session["user"]:
    return True
  else:
    return False


@app.route("/")
def get_endings():
    endings = mongo.db.endings.find().sort("ending_date", -1).limit(3)
    ratings = mongo.db.endings.find().sort("rating", -1).limit(3)

    return render_template("home.html", endings=endings, ratings=ratings)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    endings = list(mongo.db.endings.find({"$text": {"$search": query}}))

    return render_template("endings.html", endings=endings)


@app.route("/ending/<ending_id>/view")
def ending_detail(ending_id):
  ending = None
  try:
    ending = mongo.db.endings.find_one({"_id": ObjectId(ending_id)})
  except:
    return redirect(url_for("home"))
  return render_template("view.html", ending=ending)



@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile", methods=["GET", "POST"])
def profile():
    # grab the session user's username from db
    if not is_logged_in():
      return redirect(url_for("login"))

    user = mongo.db.users.find_one({"username": session["user"]})
    username = user["username"]

    endings = mongo.db.endings.find({"created_by": username})
    return render_template("profile.html", username=username, endings=endings)



@app.route("/endings")
def endings():
    endings = mongo.db.endings.find()
    return render_template("endings.html", endings=endings)


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/ending/add", methods=["GET", "POST"])
def add_ending():
  if not is_logged_in():
    return redirect(url_for('login'))

  if request.method == "POST":
    ending = {
        "genre_name": request.form.get("genre_name"),
        "ending_type": request.form.get("type_name"),
        "ending_name": request.form.get("ending_name"),
        "ending_image": request.form.get("ending_image"),
        "ending_description": request.form.get("ending_description"),
        "ending_date": datetime.now(),
        "created_by": session["user"],
        "rated": 0
    }
    mongo.db.endings.insert_one(ending)
    flash("Ending Successfully Added")
    return redirect(url_for("get_endings"))

  genres = mongo.db.genres.find().sort("genre_name", 1)
  types = mongo.db.types.find().sort("type_name", 1)
  return render_template("add.html", genres=genres, types=types)


@app.route("/ending/<ending_id>/edit", methods=["GET", "POST"])
def edit_ending(ending_id):
  if not is_logged_in():
    return redirect(url_for('login'))

  ending = None
  try:
    ending = mongo.db.endings.find_one({"_id": ObjectId(ending_id)})
  except:
    flash("Invalid ID")
    return redirect(url_for("home"))
  if request.method == "POST":
      if ending["created_by"] != session["user"]:
        flash('Unauthorized')
        return redirect(url_for("home"))

      submit = {
          "genre_name": request.form.get("genre_name"),
          "type": request.form.get("type_name"),
          "name": request.form.get("ending_name"),
          "description": request.form.get("ending_description"),
          "updated_at": datetime.now(),
          "created_by": session["user"]
      }
      mongo.db.endings.update_one({"_id": ObjectId(ending_id)}, {"$set": submit})
      flash("Ending Successfully Updated")

  genres = mongo.db.genres.find().sort("genres_name", 1)
  types = mongo.db.types.find().sort("type_name", 1)
  return render_template("edit.html", ending=ending, types=types, genres=genres)


@app.route("/ending/<ending_id>/delete")
def delete_ending(ending_id):
  # First check if logged in
   # Check if logged in user is equal to created_by user
    #Check for error as id can be tampered
    mongo.db.endings.delete_one({"_id": ObjectId(ending_id)})
    flash("Ending Successfully Deleted")
    return redirect(url_for("endings"))


@app.route("/ending/<ending_id>/upvote", methods=["GET", "POST"])
def upvote_ending(ending_id):
    #Check for logged in and ID tampering
    if request.method == "POST":
        mongo.db.endings.update({'_id': ObjectId(ending_id)}, {'$inc': {'rated': 1}})
        flash("Upvote Successful")
        ending = mongo.db.endings.find_one({"_id": ObjectId(ending_id)})

    return render_template("view.html", ending=ending, upvote='true')


@app.route("/get_genres")
def get_genres():
    genres = list(mongo.db.genres.find().sort("genre_name", 1))
    return render_template("genres.html", genres=genres)


@app.route("/add_genre", methods=["GET", "POST"])
def add_genre():
    if request.method == "POST":
        genre = {
            "genre_name": request.form.get("genre_name")
        }
        mongo.db.genres.insert_one(genre)
        flash("New Genre Added")
        return redirect(url_for("get_genres"))

    return render_template("add_genre.html")


@app.route("/edit_genre/<genre_id>", methods=["GET", "POST"])
def edit_genre(genre_id):
    if request.method == "POST":
        submit = {
            "genre_name": request.form.get("genre_name")
        }
        mongo.db.genres.update_one({"_id": ObjectId(genre_id)}, {"$set": submit})
        flash("Genre Successfully Updated")
        return redirect(url_for("get_genres"))

    genre = mongo.db.genres.find_one({"_id": ObjectId(genre_id)})
    return render_template("edit_genre.html", genre=genre)


@app.route("/delete_genre/<genre_id>")
def delete_genre(genre_id):
    mongo.db.genres.delete_one({"_id": ObjectId(genre_id)})
    flash("Genre Successfully Deleted")
    return redirect(url_for("get_genres"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)