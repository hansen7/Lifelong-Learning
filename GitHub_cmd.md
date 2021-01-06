**Clone a Repo from the Cloud to Local**

`git clone [put repo here, either https or git]` 

**Track the Local Modification**

`git status`

**Create a new branch**

`git checkout -b [any branch name]` 

**Select the modified files on stage for the commits**

`git add [filename]`

**Commit the Change to the relavant branch in the cloud**

`git commit -m "any message you want to add for this commit"` 

**Push the Commit to the cloud for either merge or review**

`git push origin [current branch name]` 

**Untrack the Modification of selected files <Single time>**

`git checkout -- [filename]`

**Untrack the Changes of Selected Files <Permantly>** [ref](https://docs.microsoft.com/en-us/azure/devops/repos/git/ignore-files?view=azure-devops&tabs=visual-studio)

``echo [filename] > .gitignore``

`git rm --cached [filename]`



**Do not use Git Pull, more use Git Fetch and Merge**

`git fetch`

`git checkout [which branch you want to fetch] -- [path/to/file]`



**Create a new branch for then merge**

`git checkout [branch name]`

`git push --set-upstream origin [branch name]`



**Recall the commit which is not pushed yet**:

`git cherry -v` -> to see the local unpushed commits





`git branch -a`-> see all the current branches

`git reset HEAD^ --soft`  

`git reset HEAD^ --hard`



`git branch -D`



```
git reset --hard <old-commit-id>
git push -f <remote-name> <branch-name>
```



**Git Stash**





**To pull the updated contents from forked repo, [ref](https://stackoverflow.com/questions/7244321/how-do-i-update-a-github-forked-repository):**

Add the remote, call it "upstream":

`git remote add upstream https://github.com/whoever/whatever.git`

Fetch all the branches of that remote into remote-tracking branches, such as upstream/master:

`git fetch upstream`

Make sure that you're on your master branch:

`git checkout master`

Rewrite your master branch so that any commits of yours that aren't already in upstream/master are replayed on top of that other branch:

`git rebase upstream/master`

or just:

`git pull upstream/master`



##### How to check the differences between local and github before the pull, [ref](https://stackoverflow.com/questions/6000919/how-to-check-the-differences-between-local-and-github-before-the-pull):

So, suppose you've got a remote called origin that refers to your GitHub repository, you would do:

`git fetch origin` 

and then do:

`git diff master origin/master`
in order to see the difference between your master, and the one on GitHub. If you're happy with those differences, you can merge them in with git merge origin/master, assuming master is your current branch.



##### Restore a deleted file

`git checkout <commit-id> <your-lost-file-name>`

