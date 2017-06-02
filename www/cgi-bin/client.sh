#!/usr/bin/python

import commands

commands.getoutput('yum install iscsi-initiator-utils -y')
commands.getoutput('iptables -F;setenforce 0')
commands.getoutput('iscsiadm --mode discoverydb --type sendtargets --portal 192.168.1.100 --discover')
commands.getoutput('iscsiadm --mode node --targetname iqn.2003-11.example.com:lalutii --portal 192.168.1.100:3260 --login')