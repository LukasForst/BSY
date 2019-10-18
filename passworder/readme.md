##### build

Go to docker image

`sudo docker run --rm -it -v $(pwd):/work python:3.6 /bin/bash`

and run build script

`./work/build.sh`

jump out of docker. it's done.
result is in `binary_get_permissions.tar.gz`