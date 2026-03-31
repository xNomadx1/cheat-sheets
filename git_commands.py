commands = """

1. Setup & Configuration
	- git --version - Show the installed Git version.
	- git config --global user.name "Your Name" - Set your global username.
	- git config --global user.email "your.email@example.com" - Set your global email.
	- git config --list - View current Git configuration values.
	- git init - Initialize a new Git repository in the current directory.
	- git clone <url> - Clone an existing repository from a remote server.

2. Status, Staging & Committing
	- git status - Show changed, staged, and untracked files.
	- git add <file> - Stage one file for the next commit.
	- git add . - Stage all modified and new files in the current directory tree.
	- git add -p - Stage changes interactively in smaller hunks.
	- git commit -m "message" - Commit staged changes with a message.
	- git commit -am "message" - Stage tracked files and commit in one step.
	- git commit --amend - Modify the last commit message or contents.

3. Branching & Switching
	- git branch - List local branches.
	- git branch -a - List local and remote branches.
	- git branch <branch-name> - Create a new branch.
	- git switch <branch-name> - Switch to an existing branch.
	- git switch -c <branch-name> - Create and switch to a new branch.
	- git checkout <branch-name> - Switch branches using the older command form.
	- git checkout -b <branch-name> - Create and switch using the older command form.
	- git branch -d <branch-name> - Delete a merged local branch.
	- git branch -D <branch-name> - Force delete a local branch.

4. Merging, Rebasing & Cherry-Picking
	- git merge <branch-name> - Merge another branch into the current branch.
	- git merge --squash <branch-name> - Merge changes as one commit without merge history.
	- git rebase <branch> - Replay current branch commits on top of another branch.
	- git rebase -i HEAD~n - Interactively edit, reorder, or squash recent commits.
	- git cherry-pick <commit> - Apply one specific commit onto the current branch.
	- git mergetool - Open the configured merge conflict resolution tool.

5. Remotes & Syncing
	- git remote -v - List configured remotes.
	- git remote add origin <url> - Add a remote named origin.
	- git fetch - Download changes from remotes without merging.
	- git pull - Fetch and merge changes from the tracked remote branch.
	- git pull --rebase - Fetch and rebase instead of merging.
	- git push origin <branch-name> - Push a branch to a remote.
	- git push -u origin <branch-name> - Push and set upstream tracking.
	- git push origin --delete <branch-name> - Delete a remote branch.

6. History & Inspection
	- git log - Show commit history.
	- git log --oneline - Show a compact one-line history.
	- git log --graph --oneline --all - Show all branches in a graph view.
	- git show <commit> - Show details for a specific commit.
	- git diff - Show unstaged working tree changes.
	- git diff --staged - Show staged changes.
	- git diff <branch1>..<branch2> - Compare two branches.
	- git blame <file> - Show who last changed each line in a file.

7. Stashing & Temporary Work
	- git stash - Save uncommitted changes temporarily.
	- git stash push -m "message" - Save a named stash entry.
	- git stash list - List saved stash entries.
	- git stash show -p stash@{0} - Show the patch stored in a stash.
	- git stash pop - Apply the latest stash and remove it.
	- git stash apply stash@{0} - Apply a specific stash without deleting it.
	- git stash drop stash@{0} - Delete one stash entry.
	- git stash clear - Remove all stash entries.

8. Undoing & Recovery
	- git restore <file> - Discard unstaged changes in a file.
	- git restore --staged <file> - Unstage a file but keep working tree changes.
	- git restore --staged --worktree <file> - Discard both staged and unstaged changes.
	- git reset HEAD <file> - Unstage a file using the older command form.
	- git reset --soft HEAD~1 - Undo the last commit but keep changes staged.
	- git reset --hard HEAD~1 - Undo the last commit and discard changes.
	- git reflog - Show recent HEAD movements for recovery.
	- git reset --hard <commit-id> - Reset to a specific commit with data loss.

9. Tags, Cleanup & Maintenance
	- git tag - List tags.
	- git tag <version> - Create a lightweight tag.
	- git tag -a <version> -m "message" - Create an annotated tag.
	- git push --tags - Push all tags to the remote.
	- git clean -n - Preview untracked files that would be removed.
	- git clean -fd - Remove untracked files and directories.
	- git gc - Clean up unnecessary files and optimize the local repository.
	- git fsck - Check repository integrity.
"""

print(commands)
