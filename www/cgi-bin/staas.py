#!/usr/bin/python
import commands , cgi

print "content-type:text/html\r\n\r\n"

data = cgi.FieldStorage()

storage_type = data.getvalue("type")

fos='''
<form action = "/cgi-bin/fos.py" method ="POST" >
Enter the drive name--<input type = 'text' name = 'd_name'  /><br/><br/>
Enter the drive size in MBs -- <input type = 'text' name = 'd_size' /><br/><br/>
<input type = "hidden" value = "fos" name = "st_type" >
<input type = "submit" value = "Proceed">
<input type = "reset" />	<br/><br/><br/><br/>
</form>


<form action = "/cgi-bin/smb.py" method ="POST" >
<b>For windows----<b><br/><br/><br/>
Enter the drive name--<input type = 'text' name = 'd_name'  /><br/><br/>
Enter the drive size in MBs -- <input type = 'text' name = 'd_size' /><br/><br/>
Enter the password --- <input type = 'password' name = 'passwd' /><br/><br/>
<input type = "hidden" value = "fos" name = "st_type" >
<input type = "submit" value = "Proceed">
<input type = "reset" />	
</form>
'''

dos='''
<form action = "/cgi-bin/dos.py" method ="POST" >
<input type = 'radio' name = 'selection' value = 'new' />New Drive<br/><br/>
<input type = 'radio' name = 'selection' value = 'extend'/>Extend size<br/><br/>
<input type = "hidden" value = "dos" name = "st_type" >
<input type = "submit" value = "Proceed">
<input type = "reset" />	
</form>
'''

bs='''
<form action = "/cgi-bin/bs.py" method ="POST">
Enter the name of Hard disk<input type = 'text' name = 'name'/><br/><br/>
Enter the size of Hard disk<input type = 'text' name ='size'/><br/><br/><br/>
<input type = 'submit' value = 'PROCEED'/>
<input type ="reset" value = 'RESET'/>
</form>
'''


if storage_type == "fos":
	print fos





elif storage_type == "dos":
	print dos





elif storage_type == "bs":
	print bs



