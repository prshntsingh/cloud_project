#!/usr/bin/python
 
import cgi , commands

print "Content-type:text/html\r\n\r\n"

data = cgi.FieldStorage()
 
service = data.getvalue("service")

if service == "saas":
	print ''' <meta http-equiv= "refresh" content = "1;url = /saas.html"/> '''
elif service == "paas":
	print ''' <meta http-equiv= "refresh" content = "1;url = /paas.html"/> '''
elif service == "staas":
	print '''<meta http-equiv = "refresh" content = "1;url = /staas.html"/> '''
elif service == "iaas":
	print '''<meta http-equiv = "refresh" content = "1;url = /iaas.html"/> '''
else :
	print '''<script> alert("CHOOSE SOMETHING") </script>'''

