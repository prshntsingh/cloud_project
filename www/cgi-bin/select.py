#!/usr/bin/python
 
import cgi , commands

print "Content-type:text/html\r\n\r\n"
print ""

data = cgi.FieldStorage()
 
service = data.getvalue("service")

if service == "saas":
	print ''' <meta http-equiv= "refresh" content = "1;url = http://192.168.1.100/saas.html"/> '''
elif service == "paas":
	print ''' <meta http-equiv= "refresh" content = "1;url = http://192.168.1.100/paas.html"/> '''
elif service == "staas":
	print '''<meta http-equiv = "refresh" content = "1;url = http://192.168.1.100/staas.html"/> '''
elif service == "iaas":
	print '''<meta http-equiv = "refresh" content = "1;url = http://192.168.1.100/iaas.html"/> '''
else :
	print '''<script> alert("CHOOSE SOMETHING") </script>'''

