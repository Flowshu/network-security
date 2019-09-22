#! /usr/bin/env python

import itertools
from telnetlib import Telnet

# connect to license server
connection = Telnet("localhost",1337)

# generate all possible keys
for key in itertools.product("0123456789", repeat=8):
    # send key to server ...
    connection.write(''.join(key))
    # and wait for response
    response = connection.read_until('\n')
    if 'SERIAL_VALID=1' in response:
        print('Found valid key!')
        print('Key: ' + ''.join(key))