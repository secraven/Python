#!/usr/bin/env python

import hashlib
import paramiko
from paramiko import rsakey


file1 = open('/root/wordlists/100-common-passwords.txt', 'r')
Lines = file1.readlines()

file2 = open('/root/hashedvalues.txt', 'w')

for i in Lines:
        md5hash = hashlib.md5(i.encode())
        file2.write(md5hash.hexdigest())
        file2.write("\n")


file2.close()

file3 = open('/root/hashedvalues.txt', 'r')

Hashed = file3.readlines()


kf = open('/root/id_rsa', 'r')

for hash in Hashed:
        kf.seek(0)
        try:
                nk = rsakey.RSAKey.from_private_key(kf, password=hash.rstrip())
                print("Success", hash)
        except paramiko.ssh_exception.SSHException:
                print("Fail", hash.rstrip())
