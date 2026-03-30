commands = """

1. Navigation & Files
	- pwd - Show the current directory.
	- ls - List files in the current directory.
	- ls -la - List all files, including hidden ones, with details.
	- cd <dir> - Change into a directory.
	- cd .. - Move up one directory.
	- cd ~ - Go to the home directory.
	- mkdir <dir> - Create a new directory.
	- touch <file> - Create an empty file.
	- cp <src> <dest> - Copy a file.
	- mv <src> <dest> - Move or rename a file.
	- rm <file> - Delete a file.
	- rm -r <dir> - Delete a directory and its contents.

2. Viewing File Contents
	- cat <file> - Print a file's contents.
	- less <file> - View a file one screen at a time.
	- head <file> - Show the first 10 lines of a file.
	- tail <file> - Show the last 10 lines of a file.
	- tail -f <file> - Follow a file as new lines are added.
	- nl <file> - Show file contents with line numbers.
	- wc <file> - Count lines, words, and bytes in a file.

3. Searching
	- find <path> -name "<name>" - Find files by name.
	- grep "<text>" <file> - Search for text in a file.
	- grep -R "<text>" <dir> - Search recursively in a directory.
	- rg "<text>" - Fast recursive text search with ripgrep.
	- which <command> - Show the path to a command.
	- whereis <command> - Show binary, source, and man page locations.

4. Permissions & Ownership
	- chmod +x <file> - Make a file executable.
	- chmod 644 <file> - Set common read/write permissions for a file.
	- chmod 755 <dir> - Set common directory permissions.
	- chown <user>:<group> <file> - Change file owner and group.
	- sudo <command> - Run a command as administrator.

5. Processes & System Info
	- ps aux - List running processes.
	- top - Live process viewer.
	- htop - Interactive process viewer, if installed.
	- kill <pid> - Stop a process by PID.
	- kill -9 <pid> - Force kill a process.
	- uname -a - Show kernel and system information.
	- hostname - Show the system hostname.
	- whoami - Show the current user.
	- id - Show user and group IDs.
	- df -h - Show disk usage by filesystem.
	- du -sh <dir> - Show total size of a directory.
	- free -h - Show memory usage.

6. Networking
	- ip a - Show network interfaces and addresses.
	- ping <host> - Test connectivity to a host.
	- curl <url> - Fetch a URL from the command line.
	- wget <url> - Download a file from a URL.
	- ss -tulpn - Show listening ports and processes.
	- ssh user@host - Connect to a remote machine over SSH.
	- scp <file> user@host:<path> - Copy a file to a remote machine.

7. Archives & Compression
	- tar -czf archive.tar.gz <dir> - Create a compressed tar archive.
	- tar -xzf archive.tar.gz - Extract a compressed tar archive.
	- zip -r archive.zip <dir> - Create a zip archive.
	- unzip archive.zip - Extract a zip archive.

8. Package Management (Debian/Ubuntu)
	- sudo apt update - Refresh package lists.
	- sudo apt upgrade - Install available package upgrades.
	- sudo apt install <package> - Install a package.
	- sudo apt remove <package> - Remove a package.
	- sudo apt autoclean - Remove cached package files that can no longer be downloaded.
	- apt search <package> - Search for a package.

9. Shortcuts & Terminal Control
	- clear - Clear the terminal screen.
	- history - Show command history.
	- Ctrl+C - Stop the current command.
	- Ctrl+D - Exit the current shell.
	- Ctrl+L - Clear the terminal screen.
	- Tab - Auto-complete commands and paths.

10. Useful Combo Commands
	- command --help - Show command usage help.
	- man <command> - Open the manual page for a command.
	- <command> | less - Pipe output into a pager.
	- <command> > file.txt - Redirect output into a file.
	- <command> >> file.txt - Append output to a file.
	- <command1> | <command2> - Send output from one command into another.
"""

print(commands)
