commands = """

1. Navigation & Files
	- pwd - Show the current directory.
	- ls - List files in the current directory.
	- ls -la - List all files, including hidden ones, with details.
	- tree - Show files and folders in a tree view, if installed.
	- cd <dir> - Change into a directory.
	- cd .. - Move up one directory.
	- cd ~ - Go to the home directory.
	- mkdir <dir> - Create a new directory.
	- mkdir -p <dir>/<subdir> - Create nested directories in one command.
	- *rmdir <dir> - Remove an empty directory.
	- touch <file> - Create an empty file.
	- cp <src> <dest> - Copy a file.
	- cp -r <src> <dest> - Copy a directory recursively.
	- mv <src> <dest> - Move or rename a file.
	- *rm <file> - Delete a file.
	- *rm -r <dir> - Delete a directory and its contents.
	- ln -s <target> <link> - Create a symbolic link.
	- file <name> - Show a file's type.
	- stat <file> - Show detailed file metadata.
	- realpath <file> - Show the absolute path of a file.

2. Viewing File Contents
	- cat <file> - Print a file's contents.
	- less <file> - View a file one screen at a time.
	- head <file> - Show the first 10 lines of a file.
	- head -n 20 <file> - Show the first 20 lines of a file.
	- tail <file> - Show the last 10 lines of a file.
	- tail -f <file> - Follow a file as new lines are added.
	- nl <file> - Show file contents with line numbers.
	- wc <file> - Count lines, words, and bytes in a file.
	- sort <file> - Sort lines in a file.
	- uniq <file> - Remove adjacent duplicate lines.
	- cut -d ',' -f1 <file> - Extract a column using a delimiter.
	- sed -n '1,20p' <file> - Print a specific line range from a file.
	- awk '{print $1}' <file> - Print the first column from each line.

3. Searching
	- find <path> -name "<name>" - Find files by name.
	- find <path> -type f - Find only files.
	- find <path> -type d - Find only directories.
	- grep "<text>" <file> - Search for text in a file.
	- grep -n "<text>" <file> - Search with line numbers.
	- grep -R "<text>" <dir> - Search recursively in a directory.
	- rg "<text>" - Fast recursive text search with ripgrep.
	- locate <name> - Search the file database for matching paths.
	- which <command> - Show the path to a command.
	- whereis <command> - Show binary, source, and man page locations.
	- xargs - Build and run commands from standard input.

4. Permissions & Ownership
	- chmod +x <file> - Make a file executable.
	- chmod 644 <file> - Set common read/write permissions for a file.
	- chmod 755 <dir> - Set common directory permissions.
	- chmod -R 755 <dir> - Change permissions recursively.
	- chown <user>:<group> <file> - Change file owner and group.
	- chgrp <group> <file> - Change a file's group.
	- umask - Show the default permission mask.
	- sudo <command> - Run a command as administrator.

5. Users & Groups
	- whoami - Show the current user.
	- id - Show user and group IDs.
	- groups - Show the groups for the current user.
	- who - Show logged-in users.
	- w - Show logged-in users and what they are doing.
	- passwd - Change your password.
	- sudo useradd -m <user> - Create a new user with a home directory.
	- sudo usermod -aG <group> <user> - Add a user to a group.
	- *sudo userdel -r <user> - Delete a user and their home directory.

6. Processes & System Info
	- ps aux - List running processes.
	- top - Live process viewer.
	- htop - Interactive process viewer, if installed.
	- pgrep <name> - Find process IDs by name.
	- pkill <name> - Kill processes by name.
	- kill <pid> - Stop a process by PID.
	- kill -9 <pid> - Force kill a process.
	- uptime - Show how long the system has been running.
	- uname -a - Show kernel and system information.
	- hostname - Show the system hostname.
	- lscpu - Show CPU information.
	- lsmem - Show memory block information, if available.
	- df -h - Show disk usage by filesystem.
	- du -sh <dir> - Show total size of a directory.
	- free -h - Show memory usage.
	- env - Show environment variables.
	- printenv <VAR> - Show the value of one environment variable.

7. Services & Logs
	- systemctl status <service> - Show the status of a service.
	- sudo systemctl start <service> - Start a service.
	- sudo systemctl stop <service> - Stop a service.
	- sudo systemctl restart <service> - Restart a service.
	- sudo systemctl enable <service> - Enable a service at boot.
	- journalctl -u <service> - Show logs for a service.
	- journalctl -xe - Show recent system log messages with detail.
	- dmesg - Show kernel ring buffer messages.

8. Networking
	- ip a - Show network interfaces and addresses.
	- ip route - Show the routing table.
	- ping <host> - Test connectivity to a host.
	- curl <url> - Fetch a URL from the command line.
	- curl -I <url> - Fetch only HTTP headers.
	- wget <url> - Download a file from a URL.
	- ss -tulpn - Show listening ports and processes.
	- dig <domain> - Query DNS records, if installed.
	- nslookup <domain> - Look up DNS information.
	- traceroute <host> - Trace the network path to a host.
	- ssh user@host - Connect to a remote machine over SSH.
	- scp <file> user@host:<path> - Copy a file to a remote machine.
	- rsync -av <src> <dest> - Copy files efficiently while preserving metadata.

9. Disks, Mounts & Storage
	- lsblk - Show block devices and partitions.
	- blkid - Show block device UUIDs and filesystem types.
	- mount - Show mounted filesystems.
	- sudo mount <device> <dir> - Mount a device to a directory.
	- sudo umount <device-or-dir> - Unmount a mounted device or directory.
	- fdisk -l - List disks and partitions.

10. Archives & Compression
	- tar -czf archive.tar.gz <dir> - Create a compressed tar archive.
	- tar -xzf archive.tar.gz - Extract a compressed tar archive.
	- tar -tf archive.tar.gz - List the contents of a tar archive.
	- gzip <file> - Compress a file into .gz format.
	- gunzip <file.gz> - Decompress a .gz file.
	- zip -r archive.zip <dir> - Create a zip archive.
	- unzip archive.zip - Extract a zip archive.

11. Package Management
	- sudo apt update - Refresh package lists.
	- sudo apt upgrade - Install available package upgrades.
	- sudo apt install <package> - Install a package.
	- *sudo apt remove <package> - Remove a package.
	- sudo apt autoclean - Remove cached package files that can no longer be downloaded.
	- apt search <package> - Search for a package.
	- sudo dnf install <package> - Install a package on Fedora/RHEL systems.
	- sudo dnf upgrade - Upgrade packages on Fedora/RHEL systems.
	- sudo pacman -S <package> - Install a package on Arch Linux.
	- sudo pacman -Syu - Refresh package databases and upgrade on Arch Linux.

12. Shortcuts & Terminal Control
	- clear - Clear the terminal screen.
	- reset - Reset a broken terminal session.
	- history - Show command history.
	- Ctrl+C - Stop the current command.
	- Ctrl+D - Exit the current shell.
	- Ctrl+L - Clear the terminal screen.
	- Tab - Auto-complete commands and paths.

13. Useful Combo Commands
	- command --help - Show command usage help.
	- man <command> - Open the manual page for a command.
	- <command> | less - Pipe output into a pager.
	- <command> > file.txt - Redirect output into a file.
	- <command> >> file.txt - Append output to a file.
	- <command> 2> errors.txt - Redirect errors into a file.
	- <command> > output.txt 2>&1 - Redirect stdout and stderr into one file.
	- <command1> | <command2> - Send output from one command into another.
"""

print(commands)
