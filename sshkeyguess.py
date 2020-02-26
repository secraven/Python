#!/usr/bin/env python

import paramiko
from paramiko import rsakey

kf = open("/root/Documents/mysamplekey", "r")

dlist = ["foo", "bar", "foobar", "klunssi", "xyzzy", "password"]

for d in dlist:
    kf.seek(0)
    try:
        nk = rsakey.RSAKey.from_private_key(kf, password=d)
        print("success", d)
    except paramiko.ssh_exception.SSHException:
        print("fail", d)