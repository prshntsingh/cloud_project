#!/usr/bin/python
import commands

commands.getoutput('mkdir /media/ll')
commands.getoutput('yum install cifs-utils -y')
commands.getoutput('yum install samba-client -y')
commands.getoutput('mount -t cifs -o username=ll  //192.168.1.100/ll /media/ll')
commands.getoutput('systemctl restart rpcbind ')
commands.getoutput('iptables -F;setenforce 0')