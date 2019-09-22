#! /bin/bash

for port in {5000..6000}; do
	echo $port;
	echo "GET / HTTP/1.1" | nc 127.0.0.1 $port; >> out;
done;
cat out | grep -B 10 'html';
