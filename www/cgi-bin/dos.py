#!/usr/bin/python
import commands , cgi
print "content-type:text/html\r\n\r\n"
data = cgi.FieldStorage()
option = data.getvalue("selection")
new='''
<form action = "/cgi-bin/fos.py" method ="POST" >
Enter the drive name--<input type = 'text' name = 'd_name'  /><br/><br/>
Enter the drive size in MBs -- <input type = 'text' name = 'd_size' /><br/><br/>
<input type = "hidden" value = "fos" name = "st_type" >
<input type = "submit" value = "Proceed">
<input type = "reset" />	
</form>
'''

ext='''
<form action = "/cgi-bin/ext.py" method ="POST">
Enter the valid drive name--<input type = 'text' name = 'd_name'  /><br/><br/>
Enter the size to be added in MBs -- <input type = 'text' name = 'd_size' /><br/><br/>
<input type = "hidden" value = "fos" name = "st_type" >
<input type = "submit" value = "Proceed">
<input type = "reset" />	
</form>
'''

if option == 'new':
	print new
#	print "<meta http-equiv='refresh' content='0;url=/fos.py'/>"

elif option == 'extend':
	print ext
