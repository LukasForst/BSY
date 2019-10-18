 #!/bin/bash

timestamp=$(date "+%Y%m%d%H%M%S")
for filename in logs/*.log; do
    [ -f "$filename" ] || continue
    openssl rsautl -encrypt -inkey public_key.pem -pubin -in "$filename" -out "$filename-${timestamp}.enc"
    truncate -s 0 "$filename"
done

