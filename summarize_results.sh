#!/usr/bin/env bash

FILE=$1

egrep -v 'error|Bad Request' $FILE | cut -d' ' -f2 | sort | uniq -c | xargs -I{} echo "Version" {} | sed 's/Version://' | awk '{print $1 " " $3 " " $2 }'

grep "Bad Request" $FILE | cut -d: -f 2 | cut -d' ' -f2 | sort | uniq -c | xargs -I {} echo "Bad Request" {} | awk '{print $1 $2 " " $4 " " $3}'

for i in NameResolutionError SSLError NewConnectionError
do
  echo "Error ${i}" $(grep error $FILE | grep ${i} | wc -l )
done
