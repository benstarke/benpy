
   CREDIT CARD----MUST





#--GIT Push and Pull---

--How to perform Git PUSH and PULL requests through GitHub Desktop and the Command-Line---

#--You'll be using GitHub for this tutorial as it is widely used, however, Bitbucket, Gitlab, etc. are also popular, but Developers, Data Scientists, and Data Analysts mostly use the GitHub to PUSH and do PULL Request--


--Where developers pull and push there projects--
#--Github
#--GitLab
#--Bitbucket

--What developers use to pull and push to the named above sites--
1.Git
2.Docker
3.Kubernets
4.Jekins

#--There are different configuration levels in the Git. Configuration can be at three different levels. They are--

1.System
2.Global
3.Repository

#--You also can ensure the git's version

git --version

#--You can set up Git with your name

git config --global user.name "<Your-Full-Name>"
#--You can set up Git with your email

git config --global user.email "<your-email-address>"
#--You can make sure that Git output is colored

git config --global color.ui auto
#--You can display the original state in a conflict

git config --global merge.conflictstyle diff3
#--You can see current configurations type

git config --list



#--Git with a code Editor--

#--You can use Git with the editors(IDE) you like. There are many popular code editors out there. You can use different editors according to your choice and to do that you can use google to search for how to do so?

#--Sublime Text Setup:

git config --global core.editor "'C:/Program Files/Sublime Text 2/sublime_text.exe' -n -w"

#--VSCode Setup:

git config --global core.editor "code --wait"

#--Atom Editor Setup:

git config --global core.editor "atom --wait"








Renaming and Removing Remotes
-git remote rename pb paul
- git remote remove paul
- git remote show origin


How do I switch branches from master to main?
-To switch the default branch used to deploy apps from master to main, first create a new branch locally:

git checkout -b main
-Next, delete the old default branch locally:

git branch -D master



checkout

    git checkout [branch] switches to another branch

    git checkout -b [new-branch] creates and switches to a new branch

    git checkout -b [new-branch] [existing branch] creates and switches to a new branch based on an existing one

    git checkout -b [new-branch] [remote/branch] creates and switches to a new branch based on remote/branch

    git checkout [commit sha] checks out the state of the repository at a particular commit



MPESA INTEGRATION