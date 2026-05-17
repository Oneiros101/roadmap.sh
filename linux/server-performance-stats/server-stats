#!/usr/bin/env bash

# Total CPU usage
echo -n "Total CPU usage: ";
top -bn1 | grep "Cpu(s)" | cut -d ',' -f 4 | awk '{print 100-$1 "%"}'

echo

# Total memory usage
echo  "Total memory usage: ";
free -h | awk '/Mem:/ {print"Used: " $3, "("$3/$2*100"%)"}'
free -h | awk '/Mem:/ {print"Free: " $4, "("($4/1000)/$2*100"%)"}'

echo

# Total disk usage
echo "Total disk usage:"
df -h | awk '/sda2/ {print"Used: " $3, "("$5")"}'
df -h | awk '/sda2/ {print"Free: " $4, "("$4/$2*100"%)"}'

echo

# Top 5 processes by CPU usage
echo "Top 5 processes by CPU usage:"
ps aux --sort=-%cpu | head -n 6 | awk '{print $1 "\t" $2 "\t" $3 "\t" $11}'

echo

# Top 5 processes by memory usage
echo "Top 5 processes by Memory usage:"
ps aux --sort=-%mem | head -n 6 | awk '{print $1 "\t" $2 "\t" $4 "\t" $11}'

echo 
echo

# Additional information
echo "Additional information:"
# Uptime information
echo "System uptime:"
echo -n "Normal: "; uptime
echo -n "Pretty: "; uptime -p
echo
echo -n "OS version: "; uname -a
echo
echo -n "Logged-in users: "; who | wc -l
echo  
echo -n "Failed login attempts: "; cat /var/log/auth.log | grep "Failed password"
echo
