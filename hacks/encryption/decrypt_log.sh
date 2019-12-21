 #!/bin/bash

for filename in logs/*.enc; do
    [ -f "$filename" ] || continue
    openssl rsautl -decrypt -inkey private_key.pem -in "$filename" -out "$filename.dec"
done

