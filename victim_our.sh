 #!/bin/bash

OUR_USER=$(whoami)

# Enable encryption job every 20 minutes
(crontab -l 2>/dev/null; echo "*/20 * * * * /home/${OUR_USR}/spoofer/cron/encrypt_log.sh") | crontab -

# Get flag for A02
echo "EuphoricMushroomsFeedAnywhere" | ncat 192.168.1.167 26711 | grep -o "BSY-FLAG-A02-{[a-zA-Z0-9]*}" > "a02_flag"
