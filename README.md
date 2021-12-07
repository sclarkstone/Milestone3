set up

set up mongodb
randomkeygen for secrete code
create env file
create .gitignore file
create requirements file create procfile
set up heroku - connect via github - add config vars - automatic deployment
install flask pymongo
install dnspython
update requirements file


****** make sure to set debug to false when going live ********

Gitpod codebase change to dependancies
If you have an older version of the template:
run pip3 freeze > unins.txt && pip3 uninstall -y -r unins.txt && rm unins.txt as per @SuzyBee_lead’s instruction above
(re)install all the dependencies that your app needs (using pip3 install)
When you're confident all your dependencies are in the workspace, update requirements using pip3 freeze > requirements.txt
Save, commit, and push.
From here onwards, whenever you (re)start your workspace, you need to do two things:
run pip3 freeze > unins.txt && pip3 uninstall -y -r unins.txt && rm unins.txt first, and then
run  pip3 install -r requirements.txt second