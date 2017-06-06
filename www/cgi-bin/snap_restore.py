#!/usr/bin/python

import commands , cgi
print "content-type:text/html\r\n\r\n"

data = cgi.FieldStorage()

sn_id = data.getvalue("snap_id")
av_zone = data.getvalue("zone")


print commands.getoutput("sudo (echo AKIAJXFIJBUUP547AOWA;echo eS4O/C7AE4XUi7JKe+lgrDXYvQVVk5tFA/RCLFKe;) | aws configure")

p=commands.getoutput("sudo aws ec2 create-volume --region us-west-2 --availability-zone "+av_zone+" --snapshot-id "+sn_id)

vol_id = p[109:130]
print "volume id is "+vol_id


f = open("/var/www/html/instructions.sh","w")
f.write(p)
f.close()


print "<a href = '/instructions.sh'><button>Click to download instructions</button></a>"


