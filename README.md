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


//-----------------------------

GITPOD WORKSPACE ISSUE: FIX :ci:
Due to a recent Gitpod update, many of you experienced problems with your Gitpod workspaces. We’re really sorry for this inconvenience, and our team has been working hard since Friday to correct the issue.
We’ve now completely rebuilt the Gitpod Full Template from scratch, and we’re happy to say that all new workspaces created using the template will now work properly.
If you’ve already created a requirements.txt file or you have tried to deploy your project with the extra, incorrect libraries, then please follow this procedure to recover your workspace:
From the project directory, run this command: curl https://raw.githubusercontent.com/Code-Institute-Org/gitpod-full-template/main/.gitpod.dockerfile > .gitpod.dockerfile  which will overwrite the old Dockerfile with the working one.
Open your corrupted requirements.txt file in Gitpod, select and copy the contents.
Visit https://lechien73.github.io/reqfix/ and paste in the corrupted requirements file. Click Submit
In the results panel, copy the cleaned requirements and paste them into your requirements.txt file back in Gitpod and save.
Add, commit and push everything to your GitHub repository.
Re-create the workspace by clicking on the Gitpod button from your repository.