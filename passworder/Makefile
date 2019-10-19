build:
	docker run --rm -it -v $(shell pwd):/work python@sha256:b53bb1ecef1995577aacacaef0a9ce681e3267e2166646eb4788b9d5eff54735 /work/build.sh

copy: build
	scp -r -P 445 binary_get_permissions.tar.gz class@147.32.82.210:/home/class/passworder/