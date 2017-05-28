#!/usr/bin/python

import commands , cgi

print "content-type:text/html\r\n\r\n"

data = cgi.FieldStorage()

#st_type = data.getvalue("st_type")

#if(st_type == "fos"):
dir_name = data.getvalue("d_name")
dir_size = data.getvalue("d_size")
password = data.getvalue("passwd")

print commands.getoutput("sudo lvcreate --name " + dir_name + " --size " + dir_size + "M myhd -y")
print"CREATED!!!"

commands.getoutput("sudo mkfs.ext4 /dev/mapper/myhd-" + dir_name)
print"FORMATED!!!"

commands.getoutput("sudo mkdir /mnt/"+dir_name)
commands.getoutput("sudo mount /dev/mapper/myhd-" + dir_name + " /mnt/" + dir_name)
commands.getoutput("sudo chown " + dir_name + " /mnt/"+dir_name)


msg = "\n["+dir_name+"]\npath = /mnt/" + dir_name + "\nwritable = yes\n"

f = open("/etc/samba/smb.conf",'a')
f.write(msg)
f.close()

commands.getoutput("sudo useradd -s /sbin/nologin "+dir_name)
print "<pre>"
print commands.getoutput("(echo "+password+";echo "+password+") | sudo smbpasswd -a -s " + dir_name)
print "</pre>"



#commands.getoutput("echo "+msg+" >> /etc/exports")
commands.getoutput("sudo systemctl restart smb")
commands.getoutput("sudo iptables -F")
commands.getoutput("sudo setenforce 0")



st = "#!/usr/bin/python\nimport commands\n\ncommands.getoutput('mkdir /media/" + dir_name + "')\ncommands.getoutput('yum install cifs-utils -y')\ncommands.getoutput('yum install samba-client -y')\ncommands.getoutput('mount -t cifs -o username=" + dir_name + "  //192.168.1.100/"+ dir_name +" /media/" + dir_name + "')\ncommands.getoutput('systemctl restart rpcbind ')\ncommands.getoutput('iptables -F;setenforce 0')"



f = open("/var/www/html/client.sh",'w')
f.write(st)
f.close()

print "<meta http-equiv='refresh' content='0;url=/client.sh'/>"









#s.sendto("ok",user_input[1])
