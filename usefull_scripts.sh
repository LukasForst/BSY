# get all unique records from the log
cat get_permissions_ssh_checking/log.txt | grep -A 1 -a "access" | grep Ip | sort --unique