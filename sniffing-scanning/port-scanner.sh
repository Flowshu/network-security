#! /bin/bash

for port in {1..254}; do 
    ping -c1 127.0.0.$port;  
done;
