#!/usr/bin/python

import commands , cgi

print "content-type:text/html\r\n\r\n"

data = cgi.FieldStorage()

drive_name = data.getvalue('d_name')
drive_size = data.getvalue('d_size')

print commands.getoutput("sudo lvextend --size +" + drive_size + "M /dev/myhd/"+ drive_name )
print commands.getoutput("sudo resize2fs /dev/myhd/" + drive_name)

