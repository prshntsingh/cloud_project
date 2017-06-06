#!/usr/bin/python

import commands , cgi
print "content-type:text/html\r\n\r\n"

data = cgi.FieldStorage()

sg_name = data.getvalue("grp_name")
ami = data.getvalue("ami")
n = data.getvalue("no")
key_name = "prashantkey"

print commands.getoutput("sudo (echo AKIAJXFIJBUUP547AOWA;echo eS4O/C7AE4XUi7JKe+lgrDXYvQVVk5tFA/RCLFKe;) | aws configure")

p=commands.getoutput("sudo aws ec2 create-security-group --group-name " + sg_name + " --description 'security group'")

grp_id = p[18:-3]



if data.getvalue("22"):
	print commands.getoutput("sudo aws ec2 authorize-security-group-ingress --group-name "+sg_name+" --protocol tcp --port 22 --cidr 0.0.0.0/0")
if data.getvalue("3389"):
	commands.getoutput("sudo aws ec2 authorize-security-group-ingress --group-name "+sg_name+" --protocol tcp --port 3389 --cidr 0.0.0.0/0")
if data.getvalue("80"):
	commands.getoutput("sudo aws ec2 authorize-security-group-ingress --group-name "+sg_name+" --protocol tcp --port 80 --cidr 0.0.0.0/0")
if data.getvalue("443"):
	commands.getoutput("sudo aws ec2 authorize-security-group-ingress --group-name "+sg_name+" --protocol tcp --port 443 --cidr 0.0.0.0/0")

p=commands.getoutput("sudo aws ec2 run-instances --image-id "+ami+" --security-group-ids "+ grp_id +" --count "+ n +" --instance-type t2.micro --key-name "+ key_name +" --query 'Instances[0].InstanceId'")

ins_id = p[1:-1]


p=commands.getoutput("sudo aws ec2 describe-instances --instance-ids "+ins_id+" --query 'Reservations[0].Instances[0].PublicIpAddress'")

ip_addr = p[1:-1]

msg = "You can remote login to your linux os by following these steps:-\n\n\n	1.IP of you instance is "+ ip_addr +"\n\n	2.Now login using SSH protocol in following format:-\n	ssh -i 'PathToYourKey'  ec2-user"+ ip_addr +"\n\n\n\nYou can remote login to your linux os by following these steps:-\n\n\n	1.IP of you instance is "+ ip_addr


f = open("/var/www/html/instructions.sh","w")
f.write(msg)
f.close()


print "<a href = '/prashantkey.pem' download><button>Click to download the key</button></a><br/><br/>"
print "<a href = '/instructions.sh'><button>Click to download instructions</button></a>"







