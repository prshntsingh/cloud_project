#!/usr/bin/python

import commands , cgi
print "content-type:text/html\r\n\r\n"

data = cgi.FieldStorage()

v_id = data.getvalue("vol_id")
desc = data.getvalue("des")


print commands.getoutput("sudo (echo AKIAJXFIJBUUP547AOWA;echo eS4O/C7AE4XUi7JKe+lgrDXYvQVVk5tFA/RCLFKe;) | aws configure")

p=commands.getoutput("sudo aws ec2 create-snapshot --volume-id "+v_id+" --description '"+desc+"'")
print p

f = open("/var/www/html/instruction.sh","w")
f.write(p)
f.close()

print "<meta http-equiv='refresh' content='0;url=/instruction.sh'/>"
print "done!!"
