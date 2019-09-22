#! /bin/bash

for port in {1..254}; do 
    ping -c1 10.1.1.$port;  
done;
