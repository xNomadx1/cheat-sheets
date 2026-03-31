commands = """

1. Inspect Existing Cron Jobs
	- crontab -l - List cron jobs for the current user.
	- sudo crontab -l - List cron jobs for root.
	- crontab -u <user> -l - List cron jobs for another user, if permitted.
	- ls -la /etc/cron.d - Show system cron drop-in files.
	- ls -la /etc/cron.daily /etc/cron.weekly /etc/cron.monthly - Show periodic system job folders.
	- sudo cat /etc/crontab - View the system-wide crontab file.

2. Add, Edit & Remove Jobs
	- crontab -e - Edit the current user's crontab.
	- sudo crontab -e - Edit root's crontab.
	- crontab -u <user> -e - Edit another user's crontab, if permitted.
	- crontab <file> - Install jobs from a file.
	- crontab -l > mycron.backup - Back up the current user's crontab.
	- crontab mycron.backup - Restore a crontab from a backup file.
	- *crontab -r - Remove the current user's crontab.
	- sudoedit /etc/crontab - Edit the system-wide crontab safely.
	- sudoedit /etc/cron.d/<job-name> - Add a named system cron file.

3. Cron Schedule Syntax
	- minute, hour, day-of-month, month, day-of-week, <command> - Standard cron field order.
	- * * * * * <command> - Run every minute.
	- */5 * * * * <command> - Run every 5 minutes.
	- 0 * * * * <command> - Run at the top of every hour.
	- 0 2 * * * <command> - Run daily at 2:00 AM.
	- 0 9 * * 1-5 <command> - Run at 9:00 AM on weekdays.
	- 30 6 * * 1 <command> - Run every Monday at 6:30 AM.
	- 0 0 * * 0 <command> - Run every Sunday at midnight.
	- 0 0 1 * * <command> - Run on the first day of every month at midnight.
	- Use `*` for any value, `*/5` for every 5 units, and `1-5` for a range.
	- @reboot <command> - Run once at system startup.
	- @hourly <command> - Run once per hour.
	- @daily <command> - Run once per day.
	- @weekly <command> - Run once per week.
	- @monthly <command> - Run once per month.

4. Common Job Examples
	- */15 * * * * /usr/bin/curl -fsS https://example.com/health - Run a command every 15 minutes.
	- 0 3 * * * /usr/bin/python3 /opt/app/backup.py - Run a Python script daily at 3:00 AM.
	- 0 2 * * 0 tar -czf /tmp/site.tgz /var/www/site - Create a weekly archive.
	- 0 0 * * * cd /srv/app && ./deploy.sh >> /var/log/app-deploy.log 2>&1 - Change directory, run a script, and log output.
	- @reboot /usr/bin/flock -n /tmp/myjob.lock /srv/app/startup-task.sh - Prevent overlap at boot with a lock file.

5. Useful Cron File Patterns
	- MAILTO=you@example.com - Email job output to this address.
	- SHELL=/bin/bash - Use bash instead of the default shell.
	- PATH=/usr/local/bin:/usr/bin:/bin - Set a predictable command search path.
	- CRON_TZ=America/Los_Angeles - Set the timezone for following cron entries.
	- 0 1 * * * /usr/bin/env VAR=value /path/to/command - Run with an extra environment variable.
	- 0 1 * * * /bin/bash -lc 'source ~/.profile && /path/to/command' - Load shell setup before running a command.

6. Safer & Easier Job Management
	- flock -n /tmp/job.lock <command> - Skip a run if the previous one is still active.
	- timeout 30m <command> - Stop a long-running cron job after 30 minutes.
	- nice -n 10 <command> - Lower CPU priority for a job.
	- ionice -c2 -n7 <command> - Lower disk I/O priority for a job.
	- logger -t my-cron-job "job started" - Write a message to syslog/journald.
	- test -x /path/script.sh && /path/script.sh - Only run the script if it is executable.
	- chmod +x /path/script.sh - Make a script executable before scheduling it.

7. Troubleshooting & Verification
	- systemctl status cron - Check the cron service on Debian/Ubuntu systems.
	- systemctl status crond - Check the cron service on RHEL/Fedora systems.
	- sudo systemctl restart cron - Restart the cron service on Debian/Ubuntu systems.
	- sudo systemctl restart crond - Restart the cron service on RHEL/Fedora systems.
	- journalctl -u cron - Show cron service logs on Debian/Ubuntu systems.
	- journalctl -u crond - Show cron service logs on RHEL/Fedora systems.
	- grep CRON /var/log/syslog - Search classic syslog cron entries on Debian/Ubuntu systems.
	- grep CRON /var/log/cron - Search classic cron log files on RHEL/Fedora systems.
	- run-parts --test /etc/cron.daily - Show which scripts would run from a periodic cron directory.
	- env -i /bin/bash --noprofile --norc -c '<command>' - Test a command with a nearly empty environment like cron.

8. System Cron Layout
	- crontab -e - User crontab format does not include a username column.
	- /etc/crontab - System crontab format includes a username before the command.
	- /etc/cron.d/<job-name> - Per-file system cron entries also include a username column.
	- /etc/cron.daily - Put executable scripts here for daily runs.
	- /etc/cron.weekly - Put executable scripts here for weekly runs.
	- /etc/cron.monthly - Put executable scripts here for monthly runs.

9. Good Habits
	- Use absolute paths like /usr/bin/python3 instead of relying on PATH.
	- Redirect output to a log file with >> /path/job.log 2>&1 when silence is not acceptable.
	- Wrap complex logic in a script instead of putting long pipelines directly in crontab.
	- Quote carefully and remember that % has special meaning in crontab unless escaped as \\%.
	- Run the command manually first before scheduling it.
"""

print(commands)
