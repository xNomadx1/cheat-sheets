1. Navigation & Shell Basics
	- pwd - Show the current working directory.
	- ls - List files in the current directory.
	- ls -la - List all files, including hidden ones, with details.
	- cd <dir> - Change into a directory.
	- cd .. - Move up one directory.
	- cd ~ - Go to your home directory.
	- clear - Clear the terminal screen.
	- history - Show recent commands.

2. Files & Directories
	- mkdir <dir> - Create a new directory.
	- mkdir -p <dir>/<subdir> - Create nested directories.
	- touch <file> - Create an empty file.
	- cp <src> <dest> - Copy a file.
	- cp -r <src> <dest> - Copy a directory recursively.
	- mv <src> <dest> - Move or rename a file.
	- *rm <file> - Remove a file.
	- *rm -r <dir> - Remove a directory and its contents.
	- file <name> - Show the file type.
	- stat <file> - Show detailed file information.

3. Viewing & Reading
	- cat <file> - Print a file to the terminal.
	- less <file> - View a file one screen at a time.
	- head <file> - Show the first 10 lines of a file.
	- tail <file> - Show the last 10 lines of a file.
	- tail -f <file> - Follow a file as it changes.
	- nl <file> - Show file contents with line numbers.
	- wc <file> - Count lines, words, and bytes.
	- sort <file> - Sort lines in a file.
	- uniq <file> - Remove adjacent duplicate lines.

4. Search & Filtering
	- grep "<text>" <file> - Search for text in a file.
	- grep -R "<text>" <dir> - Search recursively in a directory.
	- grep -n "<text>" <file> - Search with line numbers.
	- rg "<text>" - Fast recursive text search with ripgrep.
	- find <path> -name "<name>" - Find files by name.
	- which <command> - Show the path to a command.
	- whereis <command> - Show binary, source, and man page locations.
	- xargs - Build and run commands from standard input.

5. Pipes & Redirection
	- <command> | less - Pipe output into a pager.
	- <command> | grep "<text>" - Filter command output.
	- <command> > file.txt - Write output to a file.
	- <command> >> file.txt - Append output to a file.
	- <command> 2> errors.txt - Write errors to a file.
	- <command> > out.txt 2>&1 - Write stdout and stderr to one file.
	- <command> | tee file.txt - Show output and save it to a file.
	- <command1> | <command2> - Send output from one command into another.

6. Variables & Environment
	- echo $HOME - Print the value of an environment variable.
	- echo $PATH - Show the command search path.
	- VAR=value - Create a shell variable.
	- export VAR=value - Create and export an environment variable.
	- unset VAR - Remove a shell variable.
	- env - Show environment variables.
	- printenv - Print environment variables.
	- alias ll='ls -la' - Create a shell alias.
	- unalias ll - Remove an alias.

7. Shortcuts & Expansion
	- `*` - Match many filenames.
	- `?` - Match a single character in filenames.
	- !! - Repeat the last command.
	- !<word> - Run the most recent command starting with that word.
	- !$ - Use the last argument from the previous command.
	- $(command) - Use command substitution inside another command.
	- Tab - Auto-complete commands and paths.
	- Ctrl+C - Stop the current command.
	- Ctrl+D - Exit the current shell.
	- Ctrl+L - Clear the screen.

8. Scripts & Execution
	- ./script.sh - Run a script in the current directory.
	- bash script.sh - Run a shell script with bash.
	- chmod +x <file> - Make a file executable.
	- source ~/.bashrc - Reload your bash config in the current shell.
	- bash -n script.sh - Check a script for syntax errors.
	- set -e - Exit a script when a command fails.
	- set -u - Treat unset variables as errors in a script.
	- set -x - Print commands as a script runs for debugging.

9. Processes & Jobs
	- ps aux - List running processes.
	- pgrep <name> - Find process IDs by name.
	- pkill <name> - Kill processes by name.
	- kill <pid> - Stop a process by PID.
	- kill -9 <pid> - Force kill a process.
	- top - Show live process activity.
	- command & - Run a command in the background.
	- jobs - Show background jobs.
	- bg - Resume a stopped job in the background.
	- fg - Bring a background job to the foreground.