 #!/bin/bash

for filename in logs/*.log; do
    [ -f "$filename" ] || continue
    openssl rsautl -encrypt -inkey public_key.pem -pubin -in "$filename" -out "$filename.enc"
    truncate -s 0 "$filename"
done

