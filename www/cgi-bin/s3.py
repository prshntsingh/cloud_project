#!/usr/bin/python
 
import cgi , commands

print "Content-type:text/html\r\n\r\n"

data = cgi.FieldStorage()
 
b_name = data.getvalue("buck_name")
region = data.getvalue("reg_name")

print commands.getoutput("sudo (echo AKIAJXFIJBUUP547AOWA;echo eS4O/C7AE4XUi7JKe+lgrDXYvQVVk5tFA/RCLFKe;) | aws configure")

p=commands.getoutput("sudo aws s3api create-bucket --bucket " + b_name + " --region "+region+" --create-bucket-configuration LocationConstraint="+region)

f = open("/var/www/html/location.sh","w")
f.write(p)
f.close()

print "<meta http-equiv = 'refresh' content = '1;url = /location.sh'/>"



