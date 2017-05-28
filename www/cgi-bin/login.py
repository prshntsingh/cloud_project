#!/usr/bin/python
import cgi

#data from login page
print "Content-type:text/html\r\n\r\n"
data =cgi.FieldStorage()
username = data.getvalue("user")
password = data.getvalue("passwd")


if username == "prshnt" and password =="hello":	
	print ''' <meta http-equiv="refresh" content="1;url=/selection.html" />'''
else:
	print '''<script>alert("Wrong attributes")</script>
		<input type = "button"  onclick="location.href = '/index.html'" value = "TRY AGAIN !!!" >'''
