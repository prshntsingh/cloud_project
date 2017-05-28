#!/usr/bin/python

import commands , cgi

print "content-type:text/html\r\n\r\n"

data = cgi.FieldStorage()

#st_type = data.getvalue("st_type")

#if(st_type == "fos"):
dir_name = data.getvalue("d_name")
dir_size = data.getvalue("d_size")

print commands.getoutput("sudo systemctl start nfs-server")
print commands.getoutput("sudo systemctl start rpcbind")
print dir_size
print dir_name
###print commands.getoutput("sudo fallocate -l " + dir_size + "M " + "/tmp/"+dir_name)
print commands.getoutput("sudo lvcreate --name " + dir_name + " --size " + dir_size + "M myhd -y")


###print "fallocate -l " + dir_size + "G " + "/tmp/"+dir_name
print"CREATED!!!"
commands.getoutput("sudo mkfs.ext4 /dev/mapper/myhd-" + dir_name)
###commands.getoutput("sudo mkfs.xfs /tmp/"+dir_name)
print"FORMATED!!!"
commands.getoutput("sudo mkdir /mnt/"+dir_name)
commands.getoutput("sudo mount /dev/mapper/myhd-" + dir_name + " /mnt/" + dir_name)
###commands.getoutput("sudo mount /tmp/"+dir_name + " /mnt/" + dir_name)
msg="\n/mnt/" + dir_name + "   *(rw,no_root_squash)"

f=open("/etc/exports",'a')
f.write(msg)
f.close()

#commands.getoutput("echo "+msg+" >> /etc/exports")
commands.getoutput("sudo systemctl restart nfs-server")
commands.getoutput("sudo systemctl enable nfs-server")
commands.getoutput("sudo systemctl restart rpcbind")
commands.getoutput("sudo exportfs -r")
commands.getoutput("sudo iptables -F")
commands.getoutput("sudo setenforce 0")

#t('systemctl start rpcbind')\ncommands.getoutput('mkdir /media/" + dir_name + "')\ncommands.getoutput('mount -t nfs 192.168.1.100:/mnt/"+dir_name+ " /media/"+dir_name+"')\ncommands.getoutput('iptables -F')\ncommands.getoutput('setenforce 0')"

st = "#!/usr/bin/python\nimport commands\n\ncommands.getoutput('mkdir /media/" + dir_name + "')\ncommands.getoutput('mount -t nfs  192.168.1.100:/mnt/"+ dir_name +" /media/" + dir_name + "')\ncommands.getoutput('systemctl restart rpcbind ')\ncommands.getoutput('iptables -F;setenforce 0')"


f = open("/var/www/html/client.sh",'w')
f.write(st)
f.close()

print "<meta http-equiv='refresh' content='0;url=/client.sh'/>"









#s.sendto("ok",user_input[1])
