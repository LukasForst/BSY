#!/bin/bash

pip install --user pexpect pyinstaller

mkdir /work/build

cp /work/get_permissions.py /work/questions.json /work/build && cd /work/build

/root/.local/bin/pyinstaller get_permissions.py

rm get_permissions.py

cd /work

tar -czvf binary_get_permissions.tar.gz build/

rm -rf /work/build