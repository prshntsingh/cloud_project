#!/usr/bin/python

import cgi,commands

print "content-type:text/html\r\n\r\n"

data = cgi.FieldStorage()

softs= data.getvalue("soft")


str= "#!/usr/bin/python\nimport os\nos.system('ssh -X -o StrictHostKeyCheking=no root@192.168.1.100 " + softs +"')"
f = open("/var/www/html/"+softs+".sh",'w')
f.write(str)
f.close

print "<meta http-equiv='refresh' content='1;url=/"+softs+".sh'/>"
 
