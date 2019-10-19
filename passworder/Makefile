build:
	docker run --rm -it -v $(shell pwd):/work python:3.6 /work/build.sh

copy: build
	scp -r -P 445 binary_get_permissions.tar.gz class@147.32.82.210:/home/class/passworder/