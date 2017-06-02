#!/usr/bin/python

import commands , cgi

print "content-type:text/html\r\n\r\n"

data = cgi.FieldStorage()

d_name = data.getvalue('name')
d_size = data.getvalue('size')

commands.getoutput('sudo yum install scsi-target-utils -y')

commands.getoutput('sudo lvcreate --name '+d_name+' --size '+d_size+'M myhd -y')


st = "\n\n<target iqn.2003-11.example.com:"+d_name+">\nbacking-store /dev/myhd/"+d_name+"\n</target>"

f = open("/etc/tgt/tgtd.conf","a")
f.write(st)
f.close()


commands.getoutput('systemctl restart tgtd')

commands.getoutput('iptables -F;setenforce 0')


msg = "#!/usr/bin/python\n\nimport commands\n\ncommands.getoutput('yum install iscsi-initiator-utils -y')\ncommands.getoutput('iptables -F;setenforce 0')\ncommands.getoutput('iscsiadm --mode discoverydb --type sendtargets --portal 192.168.1.100 --discover')\ncommands.getoutput('iscsiadm --mode node --targetname iqn.2003-11.example.com:"+d_name+" --portal 192.168.1.100:3260 --login')"



f = open("/var/www/html/client.sh",'w')
f.write(msg)
f.close()


msg = "#!/usr/bin/python\n\nimport commands\n\ncommands.getoutput('iptables -F;setenforce 0')\n\ncommands.getoutput('iscsiadm --mode node --targetname iqn.2003-11.example.com:"+d_name+" --portal 192.168.1.100:3260 --logout')"



f = open("/var/www/html/logout.sh",'w')
f.write(msg)
f.close()

#print "<meta http-equiv='refresh' content='0;url=/client.sh'/>"
print "<a href = '/client.sh'>Please Download this for login</a></br></br>"
print "<a href = '/logout.sh'>Please Download this for logout</a>"












