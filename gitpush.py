git init
git add .
git commit -m "..."
git remote origin git@github.com/username/branch-name.git
git push -u origin master



git remote set-url git@github.com/username/branch-name.git



git init
git add .
git commit -m "..."
git push -u origin master


git push <repo name> <branch name>

git push --all <REMOTE-NAME>

git push <remote> --force


git push <remote> <branch>
git push <remote> --force
git push <remote> --all
git push <remote> --tags



git checkout master
git fetch origin master
git rebase -i origin/master
# Squash commits, fix up commit messages etc.
git push origin master

---Amended force push---

# make changes to a repo and git add
git commit --amend
# update the existing commit message
git push --force origin master


---Deleting a remote branch or tag---

git branch -D branch_name
git push origin :branch_name

