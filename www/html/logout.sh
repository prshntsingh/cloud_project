#!/usr/bin/python

import commands

commands.getoutput('iptables -F;setenforce 0')

commands.getoutput('iscsiadm --mode node --targetname iqn.2003-11.example.com:pappiaa --portal 192.168.1.100:3260 --logout')