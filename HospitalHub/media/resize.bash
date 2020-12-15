 #!/bin/bash

for i in *; do
    printf "Resize $i\n"
    convert "$i" -resize 225x225! "$i"
done
