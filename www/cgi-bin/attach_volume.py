#!/usr/bin/python

import commands , cgi
print "content-type:text/html\r\n\r\n"

data = cgi.FieldStorage()

v_id = data.getvalue("vol_id")
in_id = data.getvalue("ins_id")
d_name = data.getvalue("device")


print commands.getoutput("sudo (echo AKIAJXFIJBUUP547AOWA;echo eS4O/C7AE4XUi7JKe+lgrDXYvQVVk5tFA/RCLFKe;) | aws configure")

p=commands.getoutput("sudo aws ec2 attach-volume --volume-id "+v_id+" --instance-id "+in_id+" --device /dev/sd"+d_name)

print p

print "done!!"

