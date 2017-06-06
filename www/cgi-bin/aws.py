#!/usr/bin/python

import commands , cgi
print "content-type:text/html\r\n\r\n"

data = cgi.FieldStorage()

sg_name = data.getvalue("grp_name")
ami = data.getvalue("ami")
n = data.getvalue("no")
key_name = "prashantkey"

print "---------11111----------------------------------------------------------"
print commands.getoutput("sudo (echo AKIAJXFIJBUUP547AOWA;echo eS4O/C7AE4XUi7JKe+lgrDXYvQVVk5tFA/RCLFKe;) | aws configure")
print "---------2222----------------------------------------------------------"

p=commands.getoutput("sudo aws ec2 create-security-group --group-name " + sg_name + " --description 'security group'")
print "--------3333-----------------------------------------------------------"
print p
print "--------4444444-----------------------------------------------------------"
grp_id = p[18:-3]
print "group id is "+grp_id


if data.getvalue("22"):
	print commands.getoutput("sudo aws ec2 authorize-security-group-ingress --group-name "+sg_name+" --protocol tcp --port 22 --cidr 0.0.0.0/0")
if data.getvalue("3389"):
	commands.getoutput("sudo aws ec2 authorize-security-group-ingress --group-name "+sg_name+" --protocol tcp --port 3389 --cidr 0.0.0.0/0")
if data.getvalue("80"):
	commands.getoutput("sudo aws ec2 authorize-security-group-ingress --group-name "+sg_name+" --protocol tcp --port 80 --cidr 0.0.0.0/0")
if data.getvalue("443"):
	commands.getoutput("sudo aws ec2 authorize-security-group-ingress --group-name "+sg_name+" --protocol tcp --port 443 --cidr 0.0.0.0/0")

print "---------555555----------------------------------------------------------"
p=commands.getoutput("sudo aws ec2 run-instances --image-id "+ami+" --security-group-ids "+ grp_id +" --count "+ n +" --instance-type t2.micro --key-name "+ key_name +" --query 'Instances[0].InstanceId'")
print "----------666666---------------------------------------------------------"
print p
print "-----------777777--------------------------------------------------------"
ins_id = p[1:-1]
print "instance id is "+ins_id
print "----------888888---------------------------------------------------------"

p=commands.getoutput("sudo aws ec2 describe-instances --instance-ids "+ins_id+" --query 'Reservations[0].Instances[0].PublicIpAddress'")
print "---------999999----------------------------------------------------------"
print p
print "----------1010110101---------------------------------------------------------"
ip_addr = p[1:-1]
print ip_addr
print "------------111222222-------------------------------------------------------"
#passw = aws ec2 get-password-data --instance-id  i-1234567890abcdef0 --priv-launch-key C:\Keys\MyKeyPair.pem

msg = "You can remote login to your linux os by following these steps:-\n\n\n	1.IP of you instance is "+ ip_addr +"\n\n	2.Now login using SSH protocol in following format:-\n	ssh -i 'PathToYourKey'  ec2-user"+ ip_addr +"\n\n\n\nYou can remote login to your linux os by following these steps:-\n\n\n	1.IP of you instance is "+ ip_addr
print "------------11111113333333-------------------------------------------------------"

f = open("/var/www/html/instructions.sh","w")
f.write(msg)
f.close()
print "------------11111144444444-------------------------------------------------------"

print "<a href = '/prashantkey.pem' download>Click to download the key</a><br/><br/>"
print "<a href = '/instructions.sh'>Click to download instructions</a>"

print "-----------------111111555555--------------------------------------------------"






