#---git fetch---

#The following is an example of git branch output with some demo branch names.
git branch
*master
*feature1
*debug2

#Examining the contents of the /.git/refs/heads/ directory would reveal similar output.
ls ./.git/refs/heads/
master
feature1
debug2

# Remote branch refs live in the ./.git/refs/remotes/ directory. The next example code snippet shows the branches you might see after fetching a remote repo conveniently named remote-repo:
git branch -r
# origin/master
# origin/feature1
# origin/debug2
# remote-repo/master
# remote-repo/other-feature


#Git fetch commands and options 
git fetch <remote>
git fetch <remote> <branch>
git fetch --all
git fetch --dry-run



#---git fetch a remote branch ---


https://truehost.co.ke/


#--how to get url of your gitproject--
git remote get-url origin
git remote show origin
git config --list


"Truth can only be found in one place: the code."

slack
Typescript
REST API
SMS Integration in Django and ReactNative and Firebase


Google Cloud Platform
Docker
Redis
OpenAPI
FAST API
RAPID API

Vagrant
Google cloud
Azure
Angular

git remote add origin https://github.com/benstarke/vorufa.git