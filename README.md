# BETTER ENDINGS

The live link can be found here - [site link](https://milestone-3-project-sam.herokuapp.com/)

This site is targeted at people who have watched filmes or tv series and that have been disappointed with the endings. It offers the opportunity for users to write an alternative ending (a Better Ending). All the Better Endings created can be read and upvoted by users to give the author positive feedback.

![Mock up screen shots](static/images/ScreenMockUpsFinal.png)

## User experience (UX)

### Strategy
* Defining the goals - Due to the global pandemic of Covid, over the last few years the number of new release films and tv series has been significantly reduced. This has lead to an increase in older films and tv series being streamed and re watched. This has brought back reminders of the disappointment some of these exisiting films and tv series brought in regards to the endings. Where a perfectly good or even great film can be overall let down by the ending. With demand for streaming services increased because large parts of Europe have been self-isolating or working from home due to Covid.   
* what is the idea? From this research i narrowed down my idea to having a site that could allow users to write an alternatate ending (a Better Ending) and allow other users to read and upvote, providing positive feedback to the author.
* who is the target audience? My target audience would be all people with an interest in films and tv series. From my reserach this was an ever expanding pool of potential users.
* why should it be created? Offering users the possibility to re write the ending, giving emotional closure to an otherwise frustating or disappointed feelings given from the original ending will make for a more peaceful mindset. It could be seen as a well-being exercise like meditation. 

### Scope
* features and functions - several different ways to view all of the submitted Better Endings (top 3 most recently, top 3 highest rated and a search functionality to search all titles.).
* content requirements - simple but effective. 

#### User stories

#### Admin
* Objective - what does the user want to accomplish? 
    * To view, write, edit and delete all the Better Endings from any user. Also, to view all users Better Endings and to upvote those that they feel are better then the original endings.
* Functional - what does the user need to do to accomplish the objective? whats involved?
    * Admin can log in and have instant access to manage (view, edit and delete) all Better Endings.
    * They can create new Better Endings. 
    * They can also search or browse other authors Better Endings to Upvote them.

#### Author
* Objective - what does the user want to accomplish? 
    * To write, edit and delete all the Better Endings they produced. Also, to view all users Better Endings and to upvote those that they feel are better then the original endings.
* Functional - what does the user need to do to accomplish the objective? whats involved?
    * Authors log in and have instant access to manage (view, edit and delete) their own Better Endings. 
    * They can create new Better Endings.
    * They can also search or browse other authors Better Endings to Upvote them.

#### Logged in user
* Objective - what does the user want to accomplish? 
    * To view all users Better Endings and to upvote those that they feel are better then the original endings.
* Functional (user) - what does the user need to do to accomplish the objective? whats involved?
    * They can create new Better Endings.
    * Users log in and search or browse Better Endings to Upvote them. 

#### Viewer
* Objective - what does the user want to accomplish? 
    * To view all Better Endings.
* Functional - what does the user need to do to accomplish the objective? whats involved?
    * Simply visit the site. No effort involved. Minimal clicks to get to content. 


### Structure
* how will content be organised and presented - site map
    * 3 pages for users - login, register and profile
    * 4 pages for content - home, search, view and edit

### Skeleton
![Mock up wireframe](static/images/Milestone3wireframeMockup.png)


### Surface
* Following the C.R.A.P (consistancy, repetition, alignment and proximity) design methodology the pages will all have the same nav bar, footer and color scheme. This will help create a positive user experience. 

## Design and features

### Database
* To allow users to create, locate, display, edit and delete records (CRUD functionality) the database needed to have the following tables;
    
    * users - this would be to store a password for each user and to be able to associate which users was the author of each ending.
    * endings - this would be to store the details of each endings, including the date it was submitted and a running total of how many up votes each ending has.
    * genres and types - This is to populate the genres and types options on the add new form. It would also bean option to add functionality for the admin user only to be able to add/edit/delete genres and types so hte possibility is there to easily expand the site for more variety of content. It future proofs the concept and makes it adaptable.

### Home page

* Navigation bar

    * Featured on all pages, the fully responsive bar includes Logo (links to homepage). The links available are then customised depending on which type of user is viewing. If they are not logged in and are just viewing content then the links available are Home, Log in and register. If they are logged in as Admin then the links available are Home, Profile, New Ending and Log Out. All other logged in users have the following links available; Home, Porfile, New Ending and Log Out.
    * This section will allow the user to easily navigate between pages without having to revert back to the previous page via the browsers back button.
    * The navigation bar uses a collapsed 'hamburger' style for the link on mobile devices and smaller screen sizes. 

![Large screen nav bar - Admin logged in](static/images/NavAdmin.png)
![Mobile screen nav bar](static/images/NavMobileScreen.png)


* Content

    * The home page begins with a larger header which immediatly gives the context of the site.
    * There is a dynamic link which displays depending on the results of a check to see if a user is logged in. if there is not a user session set then a link to the login/ register pages are displayed. If there is a user session set then text encouraging the user to upvote the ending if they like it is displayed.
    * Further details then provide a link so that a user can browse all the site content.
    * A row of cards display the top 3 - most recently added endings into the database.This is dynamic and will always display the most recent from all the records in the database.
    * A further row of cards display the top 3 - highest rated endings. This is dynamic and will always display the highest rated from all the records in the database. 
    * The card rows are responsive to screen size and will adjust accordingly by having the cards side by side on a larger screen size. On a smaller screen size the cards will appear below one another.
    * A default image is used for all cards where an ending image URL has not been provided.
    * The preview cards display summary information of the ending images (or default image), title, genre, type, submitted short date, rating and a link to the view page for full details.

![Large screen main content](static/images/HomeLargeScreen.png)
![Mobile screen main content](static/images/HomeMobileScreen.png)

* Footer

    * The footer section is repeated across all pages for consistancy so the user can become comfortable with the layout no matter which page they are on.
    * The footer contains links to social media accounts that open in new windows so that they can easily go back to the page they were on.


### Browse page (/endings)

* A search function allows a search for words in the titles of the endings, it displays all cards with the searched words in the titles. The reset button then displays all of the results again.
* The card rows are responsive to screen size and will adjust accordingly by having the cards side by side on a larger screen size. On a smaller screen size the cards will appear below one another.
* A default image is used for all cards where an ending image URL has not been provided.
* The preview cards display summary information of the ending images (or default image), title, genre, type, submitted short date, rating and a link to the view page for full details.


### View page

* The view page begins with a larger header which immediatly gives the context for the page.
* There is a dynamic link which displays depending on the results of a check to see if a user is logged in. if there is not a user session set then a link to the login/ register pages are displayed. If there is a user session set then text encouraging the user to upvote the ending if they like it is displayed.
* One card showing the card details from the selected ending id. 
* A default image is used for all cards where an ending image URL has not been provided.
* The card displays the full details of the ending image (or default image), title, genre, type, author, submitted full date, rating and the full better ending.
* There is a dynamic button which displays depending on the results of a check to see if a user is logged in. if there is not a user session set then the upvote button is not displayed. If there is a user session set then the upvote button is displayed. A logged in user can upvote limitless times on all endings.

### login page

* A basic form is displayed with validated username and password fields. A flash message appear if login is unsuccessful due to missing fields or incorrect details entered that do not match the details in the users table. 
* A link to the register page is displayed in case the user has not yet created an account. 

### Register page

* A basic form is displayed with validated username and password fields. A flash message appear if login is unsuccessful due to missing fields or already existing username being entered that matches the details in the users table. 
* A link to the login page is displayed in case the user has already created an account. 

### Profile page

* There is dynamic content which displays differently depending on the results of a check to see the user type and number of endings the user has submitted. If the user is 'admin' then the text reads 'Here are all the submitted better endings. View, edit and delete them here.' with a table of all the endings. If the user is non admin and has submitted previous endings then the text reads 'Here are all your submitted better endings. View, edit and delete them here.' with a table of only endings they have submitted.  Finally if the non admin user has not previously submitted any endings then the text and table is hidden. 
* A link to add a new ending is displayed to all users.
* If the table of endings is displayed, this is where the user manages the endings. The action buttons for each ending enable to user to view, edit or delete the endigs that they have access to.
* The view action button takes the user to the view page and displays the ending details of the corresponding selected ending id.
* The edit action button takes the user to the edit page and displays the ending details in the edit form of the corresponding selected ending id.
* The delete action button deletes the document from the endings table using the corresponding selected ending id.


## Testing

* [Chrome developer tools](https://developer.chrome.com/docs/devtools/) on the browser was used to see any errors on the pages.
    * Got the error '404 - unable to load favicon.ico'. The pathway on the Base.html template was incorrect. Once the correct pathway link was used this corrected the issue. 

* [Chrome developer tools](https://developer.chrome.com/docs/devtools/) device toggle toolbar was utilised to view the site via emulators of different screen sizes and devices.
    * the profile page action buttons displayed side by side which was ok on a large screen size but on a mobile screen they meant the screen had to scrolled to get to them. To resolve this i put all buttons in one column and added some CSS margin-bottom so that on a mobile screen the buttons were displayed one above the other and remained side by side on larger screen sizes.


![Chrome Lighthouse audit results](static/images/LighthouseAudit.png)

* Chrome Lighthouse audit (Chrome -> dev tools -> Lighthouse) was run to for performance, accessibility, SEO and best practices. After running the initial audit the Best Practices category only scored an amber rather then green as the rest of the categories did. The audit advised that the 'Image natural dimensions should be proportional to the display size and the pixel ratio to maximize image clarity'. After using a higher quality image for the one card that was identified this then resolved the issue. To esure this issue would not happen again i decided to add some guidance instructions to the user form where image URLs are added and to have a default image if an appropriate quality image URL could not be found by the user. 

![Chrome Lighthouse audit results second attempt](static/images/LighthouseAuditFinal.png)

* Chrome Lighthouse audit - second attempt. After making corrections from the first audit and re running the audit on the second attempt all categories were green. 

* JSHint was used to to detect errors and potential problems in your JavaScript code.

* Python -  using [pep8online](http://pep8online.com/) - app.py
    * E501:2:80:line too long (84 > 79 characters). Used brackets and new line with indentation to break up line. This corrected issue.
    * E501:122:80:line too long (81 > 79 characters) . Used brackets and new line with indentation to break up line. This corrected issue.
    * E501:189:80:line too long (83 > 79 characters). Used brackets and new line with indentation to break up line. This corrected issue.
    * E501:194:80:line too long (82 > 79 characters). Used brackets and new line with indentation to break up line. This corrected issue.
    * E501:241:80:line too long (81 > 79 characters). Used brackets and new line with indentation to break up line. This corrected issue.
    * E501:257:80:line too long (84 > 79 characters). Used brackets and new line with indentation to break up line. This corrected issue.
    * After correcting the above errors and pressing the Check again button the following message displayed 'All right'.

### User Acceptance Testing

The UAT was carried out on desktop, tablet and mobile screen sizes. The UAT was also caried out on Chrome, firefox and Edge. This was to ensure cross broswer and cross device compatability and to acieve a positive user experience. 

#### Home page

Test | Expected Outcome | Actual outcome|status
-----|------------------|----------------|--------
Images|All images appear, sized correctly with alt tags|Card images and font awesome social media icons all loaded correctly| Pass
fonts|fonts use specified google fonts| Roboto and Lanto fonts load|Pass
Nav bar|responsive navbar with varying screen sizes| Nav bar is full width with visable logo text and page links on desktop and tablet screen. On mobile screen sizes it is full width with a collapsed 'hamburger' toggle hiding the page links until pressed.|Pass 
links|internal link to remain in current window and external links to open in new tab| 'Browse' link opens internal link in same window to endings page.|Pass
Dynamic links|Internal links to open in same tab with dynamic ending id as url parameter| Card links all open correct endings page with ending id and user session check displays relevant internal link . footer social media links open in new tab to external relevant sites |Pass
Cards|responsive layout| Cards side by side on desktop and tablet screen sizes. Cards below one another on mobile screen sizes.|Pass
Cards|recently added|The 3 most recently submitted endings from endings table, ending_date are displayed.|Pass
Cards|highest rated added|The 3 most highest rated endings from endings table, rated column count are displayed.|Pass

#### Browse page

Test | Expected Outcome | Actual outcome|status
-----|------------------|----------------|--------
Images|All images appear, sized correctly with alt tags|Card images and font awesome social media icons all loaded correctly| Pass
fonts|fonts use specified google fonts| Roboto and Lanto fonts load|Pass
Nav bar|responsive navbar with varying screen sizes| Nav bar is full width with visable logo text and page links on desktop and tablet screen. On mobile screen sizes it is full width with a collapsed 'hamburger' toggle hiding the page links until pressed.|Pass 
links|internal link to remain in current window and external links to open in new tab| Home page link opens internal link in same window to Home page.|Pass
Dynamic links|Internal links to open in same tab with dynamic ending id as url parameter| Card links all open correct endings page with ending id. footer social media links open in new tab to external relevant sites |Pass
Cards|responsive layout| Cards side by side on desktop and tablet screen sizes. Cards below one another on mobile screen sizes.|Pass
Search|filters by title and reset button resets to all|searching for the term 'seven' filters to one result as expected and the reset button then shows all results|Pass

#### Login page

Test | Expected Outcome | Actual outcome|status
-----|------------------|----------------|--------
Images|All images appear, sized correctly with alt tags|Font awesome form icons and social media icons all loaded correctly| Pass
fonts|fonts use specified google fonts| Roboto and Lanto fonts load|Pass
Nav bar|responsive navbar with varying screen sizes| Nav bar is full width with visable logo text and page links on desktop and tablet screen. On mobile screen sizes it is full width with a collapsed 'hamburger' toggle hiding the page links until pressed.|Pass 
links|internal link to remain in current window and external links to open in new tab| 'Register account' link opens internal link in same window to Register page. footer social media links open in new tab to external relevant sites|Pass
Form - valid entry|validated responses to login|An existing username and password matching what is in the users table and redirects to profile page|Pass
Form - invalid entry|no responses, username that does not exist or username and password not matching to users table should not login| missing values prompt the form validation. existing 'admin' username gives 'incorrect username and/or password' flash message. less then minimum length on password prompts form validation |Pass

#### Register page

Test | Expected Outcome | Actual outcome|status
-----|------------------|----------------|--------
Images|All images appear, sized correctly with alt tags|Font awesome form icons and social media icons all loaded correctly| Pass
fonts|fonts use specified google fonts| Roboto and Lanto fonts load|Pass
Nav bar|responsive navbar with varying screen sizes| Nav bar is full width with visable logo text and page links on desktop and tablet screen. On mobile screen sizes it is full width with a collapsed 'hamburger' toggle hiding the page links until pressed.|Pass 
links|internal link to remain in current window and external links to open in new tab| 'Log in' link opens internal link in same window to Login page. footer social media links open in new tab to external relevant sites|Pass
Form - valid entry|validated responses to create new account|a unique username and password matching the minimum requirements creats account in users table and redirects to profile page with a flash message 'welcome'|Pass
Form - invalid entry|no responses, responses not meeting minimum requirements or existing username should not create an account| missing values prompt the form validation. existing 'admin' username gives 'incorrect username and/or password' flash message. less then minimum length on password prompts form validation |Pass

#### Profile page

Test | Expected Outcome | Actual outcome|status
-----|------------------|----------------|--------
Images|All images appear, sized correctly with alt tags|Font awesome social media icons all loaded correctly| Pass
fonts|fonts use specified google fonts| Roboto and Lanto fonts load|Pass
Nav bar|responsive navbar with varying screen sizes| Nav bar is full width with visable logo text and page links on desktop and tablet screen. On mobile screen sizes it is full width with a collapsed 'hamburger' toggle hiding the page links until pressed.|Pass 
links|internal link to remain in current window and external links to open in new tab| 'New better ending' link opens internal link in same window to new ending page. footer social media links open in new tab to external relevant sites|Pass
Dynamic links|Internal links to open in same tab with dynamic ending id as url parameter| Action links (view, edit and delete) all open correct pages with ending id. |Pass
Dynamic Content|display all endings for admin user or if not admin then only show the endings that the user has submitted. If no endings have been submitted then introduction sentence is modified| Admin user displays all endings. Non admin user (sclarkstone) displays the 5 that were submitted. User that has not submitted any endings (samclarkstone) displays link to create better ending only and all else is hidden on page |Pass
Delete|Delete ending document from endings table| clicking the delete button deletes the ending from the table|Pass

#### Add better ending page

Test | Expected Outcome | Actual outcome|status
-----|------------------|----------------|--------
Images|All images appear, sized correctly with alt tags|Font awesome form icons and social media icons all loaded correctly| Pass
fonts|fonts use specified google fonts| Roboto and Lanto fonts load|Pass
Nav bar|responsive navbar with varying screen sizes| Nav bar is full width with visable logo text and page links on desktop and tablet screen. On mobile screen sizes it is full width with a collapsed 'hamburger' toggle hiding the page links until pressed.|Pass 
links|internal link to remain in current window and external links to open in new tab| footer social media links open in new tab to external relevant sites|Pass
Form - valid entry|validated responses to create new ending|all required fileds (all except the image URL) filled in with minimum length of 3 on the text feilds or a selected option from the drop downs fields creates a new ending document in the endings table and redirects to the home page with a flash message 'Ending Successfully Added'|Pass
Form - invalid entry|no responses, responses not meeting minimum requirements should not create an ending| missing values prompt the form validation. less then minimum length on required text fields prompts form validation |Pass


#### Edit better ending page

Test | Expected Outcome | Actual outcome|status
-----|------------------|----------------|--------
Images|All images appear, sized correctly with alt tags|Font awesome form icons and social media icons all loaded correctly| Pass
fonts|fonts use specified google fonts| Roboto and Lanto fonts load|Pass
Nav bar|responsive navbar with varying screen sizes| Nav bar is full width with visable logo text and page links on desktop and tablet screen. On mobile screen sizes it is full width with a collapsed 'hamburger' toggle hiding the page links until pressed.|Pass 
links|internal link to remain in current window and external links to open in new tab| footer social media links open in new tab to external relevant sites|Pass
Form - valid entry|ending details visable and correct and validated responses to edit ending|All fields completed with results relevant to the edning id specified to edit. All required fileds (all except the image URL) filled in with minimum length of 3 on the text feilds or a selected option from the drop downs fields edits the correct ending document in the endings table and redirects to the home page with a flash message 'Ending Successfully Updated'|Pass
Form - invalid entry|no responses, responses not meeting minimum requirements should not edit ending| missing values prompt the form validation. less then minimum length on required text fields prompts form validation |Pass

#### View page

Test | Expected Outcome | Actual outcome|status
-----|------------------|----------------|--------
Images|All images appear, sized correctly with alt tags|Card image and font awesome social media icons all loaded correctly| Pass
fonts|fonts use specified google fonts| Roboto and Lanto fonts load|Pass
Nav bar|responsive navbar with varying screen sizes| Nav bar is full width with visable logo text and page links on desktop and tablet screen. On mobile screen sizes it is full width with a collapsed 'hamburger' toggle hiding the page links until pressed.|Pass 
links|internal link to remain in current window and external links to open in new tab| 'Browse' link opens internal link in same window to endings page.|Pass
Dynamic links|Internal links to open in same tab with dynamic ending id as url parameter| User session check displays relevant internal link to 'new ending' if user is logged in and 'login or register' if not logged in . footer social media links open in new tab to external relevant sites |Pass
Dynamic Content|Display upvote button if user session set and increase upvote by one if button clicked.|Upvote button not visable if no user logged in. Upvote button visable if any user logged in and selecting it increases the count by one in the endings document for the selected ending id and a flash messages displays, 'Upvote successful' |Pass
Cards|ending details match the ending id selected to view| multiple endings selected and each view page then displays the correct ending details that corresponds to the ending id that was selected.|Pass


#### Nav bar links

Test | Expected Outcome | Actual outcome|status
-----|------------------|----------------|--------
not logged in|Should see Home, Browse, Login and register|can see Home, Browse, Login and register| Pass
admin user logged in|Should see Home, Browse, Profile, New ending and log out|can see Home, Browse, Profile, New ending and log out| Pass
non admin user logged in|Should see Home, Browse, Profile, New ending and log out|can see Home, Browse, Profile, New ending and log out| Pass


### Validator testing

* HTML - using [W3C validator](https://validator.w3.org/nu/?doc=http%3A%2F%2Fmilestone-3-project-sam.herokuapp.com%2F) - home.html

    * 'Error: Element link is missing required attribute href.' - incorrect link used, i must have copy and pasted a link incorrectly from my milestone2 project for bootstrap instead of font awesome. Once the link was corrected the error was resolved.
    * 'Warning: Section lacks heading. Consider using h2-h6 elements to add identifying headings to all sections.' - amended the flash messages to sit inside a div rather then section. this corrected the warning.
    * 'Error: Stray start tag footer.' - the footer was outside of the closing body tag. moved the footer block inside and this corrected the error.
    *Error: An img element must have an alt attribute, except under certain condition - added alt tag to all card templates, this then corrected the error.

    * After correcting the above errors and re running the w3c validator the following message came 'Document checking completed. No errors or warnings to show'.


* CSS - using [W3C Jigsaw](https://jigsaw.w3.org/css-validator)  By direct input - /static/css/style.css. Running the w3c validator the following message came 'Congratulations! No Error Found.'.

* JavaScript using JSHint - index.html
    * 'Missing semicolon.' after reviewing the code, the missing semicolon was found to be on line 122 (where the open weathermap api data is being converted to JSON) After correcting this i then re run the validator and the issue was resolved.

### First mentor review
After the first review with my mentor some recommendations for improvements were made, they are detailed below.

* Where I only had a couple of pages my mentor helped me to put a site map together of the pages that would be needed;
     * Home page (/home or /) -> Featured endings like Top Rated, Recently added, etc
    * Endings List page (/endings) -> List of all endings, with search bar and filters
     * Ending detail page (/ending/<ending_id>/view) -> More details about the ending. Also have feature to give ratings only for logged in users.
     * Add Ending page (/ending/add) -> Form to add ending
     * Edit ending page (/ending/<ending_id>/edit) -> Form to edit ending
     * Login (/login)
     * Signup (/signup)
     * Delete ending page (/ending/<ending_id>/delete) -> Form to delete ending, only admin or users who created should be able to delete it


### Second mentor review
After the second review with my mentor some recommendations for improvements were made. I carried out these recommendations, they are detailed below.

* Padding around the Nav bar to increase its size.
* Make the header sentence shorter and increase size from a h3 to h1.
* Add an image URL to the new ending form and show images on home, search and details pages.
* Use side by side cards to show each ending rather then a table display on home and search pages.
* Add a is_logged_in function to do a check first for pages that required it. If not logged in send to login page.


### Third mentor review
After the third review with my mentor some recommendations for improvements were made. I carried out these recommendations, they are detailed below.

* add a fixed height to the cards and card images so they are all the same size
* Add verticle clamp to the title on home and search pages so that if it is longer then the fixed width of the card it will not overflow.
* Add the date and rating to the home and search cards
* add padding to footer
* make the image URL field on add new adding form optional and have a default image if url not added


### Bugs

* On the add new ending page i was unable to click or tab to the ending_image field. On inspection i found that i had ending_name in the label for. Once i corrected this to ending_image it worked as expected.
* When editing or deleting i got the error - "TypeError: 'Collection' object is not callable. If you meant to call the 'update' method on a 'Collection' object it is failing because no such method exists." I ended up getting tutor support to fix this. it turns out that remove is not a normal Mongo command, delete_one was needed instead and mongo.db.endings.update({"_id": ObjectId(ending_id)}, submit) needed to be  mongo.db.endings.update_one({"_id": ObjectId(ending_id)}, {"$set": submit}). 
* top 3 highest rated not working, it was not showing the top 3 rated. On inspection i found that in the line 'ratings = mongo.db.endings.find().sort("ratings", -1).limit(3)' I had put the incorrect name of 'ratings' but to match the table field it needed to be 'rated'.
* When carrying out UAT i realised that the admin functionality to edit and delete the genres and types would inadvertently effect the existing cards within the effected genre. As the effected cards would still exist under a non existant genre/ type. To rectify this for this project i have removed the admin functionality to add, edit and delete the genres and types and added this to the desirable features list. 
* after applying the javascript function to display only short dates on the preview cards i found all the cards were displaying the same date which did not match what was bring stored in the endings table. after looking at my javascript function i found that i was using $(".card-date") inside the function but it needed to be $(this) to get the correct one rather then just the first one. Once i corrected this all short dates displayed as expected.

## Desirable features
This site for the purpose of this milestone project is a Minimum Viable Product (MVP) and contains essential features that allow it to function. Possible deseriable features for future development include;

* The users table could be expanded to have 'user type' if there is a need for multiple admin users
* logged in users could suscribe to notifications for when a new ending is added or when an ending has been edited.
* reviews - rather then just have upvotes it could allow logged in users to offer feedback to the authors too.
* more advanced searched and filter to allow easier content searches for the user as more content is added.
* After clicking delete to have an alter to check the user wants to permenantly delete the ending.
* Allow admin to add and edit genres and types without impacting existing endings.
* consideration for the upvoting - maybe the author of the ending cannot upvote their own ending and maybe a logged in user should have a single limit for each ending. Perhaps a star rating would be better where the average of the total is used.

## Set up and Deployment

* Set up mongodb collection (milestone_3) with the following tables;

Table name | column name | column type
-----|------------------|----------------
endings|genre_name|string
endings|ending_name|string
endings|ending_description|string
endings|ending_date|Date
endings|ending_type|string
endings|created_by|string
endings|rated|Int32
endings|ending_image|string
genres|genre_name|string
types|type_name|string
users|username|string
users|password|string

* In MongoDB collection insert documents as minimum default;

Table name | column name | default content
-----|------------------|----------------
genres|genre_name|Horror
genres|genre_name|Action
genres|genre_name|Rom Com
genres|genre_name|Animation
types|type_name|Film
types|type_name|Series


* [randomkeygen](https://randomkeygen.com/) for secrete key generation.
* create env file with ip, port, secret key, mongo URI and mongo db name.
* create .gitignore file
* create requirements file
* create procfile
* set up heroku - connect via github - add config vars (to match the ones in the env file) and initiate automatic deployment
* install flask pymongo using command: 'pip3 install flask-pymongo'
* install dnspython using command: 'pip3 install dnspython'
* update requirements file
* register a new user 'admin' with a secure password. this will be your admin user account.
* Add a default image to /static/images/ for endings that don't have an image URL. 

Due to a Gitpod codebase change to dependancies that was implimented after my milestone 3 project build had begun, Code institute supplied the following instructions to be applied to fix the dependancies issues from using the code institute template;
* run command: 'pip3 freeze > unins.txt && pip3 uninstall -y -r unins.txt && rm unins.txt'
* Reinstall all the dependencies that your app needs (using pip3 install)
* Update requirements using command: 'pip3 freeze > requirements.txt'
* Save, Add, commit, and push everything to GitHub repository.

From here onwards, whenever the work space is (re)started the following two things need to be done:
* run command: 'pip3 freeze > unins.txt && pip3 uninstall -y -r unins.txt && rm unins.txt'
* run command: 'pip3 install -r requirements.txt'


Due to a Gitpod update that was implemented after my milestone 3 project build had begun, Code institute supplied the following instructions to be apllied to fix the workspace issues;
* From the project directory, run this command: 'curl https://raw.githubusercontent.com/Code-Institute-Org/gitpod-full-template/main/.gitpod.dockerfile > .gitpod.dockerfile'  which will overwrite the old Dockerfile with the working one.
* Open your corrupted requirements.txt file in Gitpod, select and copy the contents.
* Visit [Code institute Gitpod requitments file fix](https://lechien73.github.io/reqfix/) and paste in the corrupted requirements file. Click Submit
* In the results panel, copy the cleaned requirements and paste them into your requirements.txt file back in Gitpod and save.
* Save, add, commit and push everything to GitHub repository.
* Re-create the workspace by clicking on the Gitpod button from your repository.

## Credits

### Layout
* github - code institute/gitpod-full-template

* [Materialize V1.0.0](https://materializecss.com/getting-started.html)

    * navbar
    * grid layout with rows and columns
    * form controls
    * responsivness and styling
    * Cards
    
* [Code institute](https://learn.codeinstitute.net/) course material. Specifically the Task manager mini project for the log in, register and logout authentication. This module was also used to inspire the mongodb collection structure.

### Content

* The icons in the forms were taken from [Font awesome](https://fontawesome.com/)

* [google fonts](https://fonts.google.com/) was used to give the project a more professional and unique feel. Google fonts gave fonts that go together and as i had already seen the Lanto font in use on the Code institute 'love running' project and felt it fit in well with my project i went with Lant and Oswald. 

* [techsini](http://techsini.com/multi-mockup/index.php) was used to generate the multi device website mock up used in the readme file.

### Media

* The card image URLs were taken from a range of sites from a google search of the relevant filem/ tv series. 