# System Health Monitoring Script

A Bash script that displays essential system health metrics for Linux servers/workstations. It outputs CPU usage, memory usage, disk usage, top resource-consuming processes, and additional system information.

## Features

- **Total CPU usage** – Percentage of CPU in use (idle subtracted from 100).
- **Total memory usage** – Used and free memory in human‑readable format, with calculated percentages.
- **Total disk usage** – Used and free space on the specified disk (`/dev/sda2`), including usage percentage.
- **Top 5 processes** – By CPU usage and by memory usage (shows user, PID, %CPU/%MEM, and command name).
- **Additional info** – System uptime (normal + pretty), OS version, number of logged‑in users, and failed login attempts (from `/var/log/auth.log`).

## Requirements

- **Linux** operating system (relies on `/proc` filesystem and standard Linux commands).
- **Bash** 4.0 or later.
- **Installed commands**:
  - `top` (procps‑ng)
  - `free` (procps‑ng)
  - `df` (coreutils)
  - `ps` (procps‑ng)
  - `uptime` (procps‑ng)
  - `uname` (coreutils)
  - `who` (coreutils)
  - `grep`, `awk`, `cut`, `head` (standard Unix tools)
- **`/var/log/auth.log`** must exist and be readable to show failed login attempts (Ubuntu/Debian); on RHEL/CentOS use `/var/log/secure`.

## Usage

1. Save the script to a file, e.g. `health.sh`.
2. Make it executable:
   ```bash
   chmod +x health.sh
   ```
3. Run it
   ```bash
   ./health.sh
   ```

**Note**: For the results, execute as `root` or with appropriate `sudo` rights (required for reading authentication logs on some systems).

## Example Output
```
Total CPU usage: 12.3%

Total memory usage: 
Used: 3.2Gi (39.5%)
Free: 4.8Gi (59.2%)

Total disk usage:
Used: 42G (45%)
Free: 51G (54.8%)

Top 5 processes by CPU usage:
root	1234	15.2	/usr/bin/nginx
user	5678	8.7	 /usr/lib/firefox/firefox
...

Top 5 processes by memory usage:
mysql	9876	12.3	/usr/sbin/mysqld
...

Additional information:
System uptime:
Normal: 14:23:15 up 3 days, 2:15, 2 users, load average: 0.08, 0.03, 0.01
Pretty: up 3 days, 2 hours, 15 minutes

OS version: Linux hostname 5.15.0-86-generic #96-Ubuntu SMP ...

Logged-in users: 2

Failed login attempts: (list of failed login entries)
```

## Known Limitations & Improvements

- Memory percentage calculation uses free -h (human‑readable values). Because $3 and $2 may contain suffixes like Gi, Mi, the arithmetic $3/$2*100 will fail (e.g., 3.2Gi/7.8Gi is not a valid number). For accurate percentages, use free -b or free -k and parse raw numbers.

- Disk usage hard‑codes the device /sda2. This may not exist on every system. A more robust script would detect the root filesystem automatically using df / and extract its device.

- Failed login attempts reads the whole auth log, which can be huge. Consider using grep -c "Failed password" /var/log/auth.log | tail -1 to get only the count, or sudo journalctl _COMM=sshd ... on systemd‑based systems.

# Project URL
https://roadmap.sh/projects/server-stats
