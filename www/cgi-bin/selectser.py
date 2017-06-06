#!/usr/bin/python
 
import cgi , commands

print "Content-type:text/html\r\n\r\n"

data = cgi.FieldStorage()
 
service = data.getvalue("service")

if service == "ec2":
	print ''' <meta http-equiv= "refresh" content = "1;url = /ec2.html"/> '''
elif service == "ebs":
	print ''' <meta http-equiv= "refresh" content = "1;url = /ebs.html"/> '''
elif service == "s3":
	print '''<meta http-equiv = "refresh" content = "1;url = /s3.html"/> '''
elif service == "elb":
	print '''<meta http-equiv = "refresh" content = "1;url = /elb.html"/> '''
else :
	print '''<script> alert("CHOOSE SOMETHING") </script>'''

