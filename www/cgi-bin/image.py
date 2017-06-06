#!/usr/bin/python

import cgi ,commands

print "content-type:text/html\r\n\r\n"

data = cgi.FieldStorage()

ins_id = data.getvalue("instance_id")
img_name = data.getvalue("name")
print commands.getoutput("sudo (echo AKIAJXFIJBUUP547AOWA;echo eS4O/C7AE4XUi7JKe+lgrDXYvQVVk5tFA/RCLFKe;) | aws configure")
p=commands.getoutput("sudo aws ec2 create-image --instance-id " + ins_id + " --name " + img_name + " --no-reboot")

ami=p[18:-3]
msg = "\n\n\n\n\n        The ami is -- '"+ami+"' use this to create new instance\n\n\n\n\n         THANK YOU!!!!"


f = open("/var/www/html/instruction.sh","w")
f.write(msg)
f.close()
 
print '''<a href = /instruction.sh><button>CLICK HERE TO DOWNLOAD AMI id</button></a>'''

