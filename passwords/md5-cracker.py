#! /usr/bin/env python

import md5
import itertools
import string

salt = '8kofferradio'
md5sum = '2b2935865b8a6749b0fd31697b467bd7'
alphabet = string.ascii_lowercase + '1234567890'

# for each possible password length ...
for pw_length in range(1,7):
    # generate all possible passwords from the alphabet ...
    for pw in itertools.product(alphabet, pw_length):
        # hash them with the given salt ...
        m = md5.new()
        m.update(salt + ''.join(pw))
        # and print the password if the hash matches the given md5sum
        if m.hexdigest() == md5sum:
            print('Click!')
            print('Password: ' + ''.join(pw))
            exit()
print('No password found.')
