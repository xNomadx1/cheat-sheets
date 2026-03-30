commands = """

1. Setup & Configuration
	- git config --global user.name "Your Name" – Set your global username.
	- git config --global user.email "your.email@example.com" – Set your global email.
	- git config --list – View all current Git configurations.
	- git init – Initialize a new Git repository in the current directory.
	- git clone <url> – Clone an existing repository from a remote server (e.g., GitHub). 

2. Basic Workflow (Staging & Committing)
	- git status – Check the status of files (modified, staged, untracked).
	- git add <file> – Stage a specific file for commit.
	- git add . – Stage all modified and new files.
	- git add -p – Stage changes interactively (patch mode).
	- git commit -m "message" – Commit staged changes with a descriptive message.
	- git commit -am "message" – Stage all tracked files and commit in one step. 

3. Branching & Merging
	- git branch – List all local branches (current branch marked with *).
	- git branch -a – List all local and remote branches.
	- git branch <branch-name> – Create a new branch.
	- git checkout <branch-name> – Switch to an existing branch.
	- git checkout -b <branch-name> – Create and switch to a new branch.
	- git switch <branch-name> – Modern alternative to checkout for switching branches.
	- git switch -c <branch-name> – Create and switch to a new branch (preferred syntax).
	- git merge <branch-name> – Merge changes from a branch into the current branch.
	- git merge --squash <branch-name> – Merge changes as a single commit.
	- git branch -d <branch-name> – Delete a branch (safe, prevents deletion if unmerged).
	- git branch -D <branch-name> – Force delete a branch (even if unmerged). 

4. Remote Operations
	- git remote -v – List all remote repositories.
	- git remote add origin <url> – Add a remote repository (e.g., GitHub).
	- git push origin <branch-name> – Push a local branch to a remote.
	- git push -u origin <branch-name> – Push and set up tracking (only needed once).
	- git push origin --delete <branch-name> – Delete a remote branch.
	- git pull – Fetch and merge changes from the remote repository.
	- git fetch – Download changes from remote without merging. 

5. Viewing History & Differences
	- git log – Show commit history.
	- git log --oneline – Show concise commit history.
	- git log --graph – Show history with branching and merging.
	- git log --oneline --graph --all – Show full history with graph across all branches.
	- git diff – Show unstaged changes (working directory vs staging area).
	- git diff --staged – Show staged changes (staging area vs last commit).
	- git show <commit> – Show details of a specific commit.
	- git blame <file> – Show who last modified each line of a file. 

6. Undoing & Repairing
	- git reset HEAD <file> – Unstage a file (keep changes in working directory).
	- git reset --hard HEAD~1 – Undo the last commit and discard changes.
	- git restore <file> – Discard changes to a file (unstaged).
	- git restore --staged --worktree <file> – Discard both staged and unstaged changes.
	- #git reset HEAD^ – Undo the last commit but keep changes staged.
	- git commit --amend – Modify the last commit (message or changes).
	- git reflog – View all actions performed on the repository (useful for recovery).
	- git reset --hard <commit-id> – Reset to a specific commit (use with caution). 
Stashing
	- git stash – Temporarily save uncommitted changes.
	- git stash pop – Apply the latest stashed changes and remove them from stash.
	- git stash list – List all stashed changes.
	- git stash clear – Remove all stashed changes. 

7. Advanced (Intermediate)
	- git rebase <branch> – Reapply commits on top of another branch (cleaner history).
	- git rebase -i HEAD~n – Interactive rebase to edit, squash, or reorder commits.
	- git cherry-pick <commit> – Apply a specific commit from one branch to another.
	- git tag <version> – Create a tag for a specific commit (e.g., v1.0).
	- git push --tags – Push all tags to remote.
	- git push --force-with-lease – Force push with safety check (recommended over --force). 
"""

print(commands)
