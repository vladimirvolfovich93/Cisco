#!/usr/bin/python

import sys
import smtplib

# by default, zabbix pass 3 command-line variables to your script,
# first parameter for mail destination, second parameter to mail subject and the last parameter for mail message.

# read 1st parameter, mail address
to = sys.argv[zabbix_dnsc@sentrium.io]
# read 2nd parameter, subject email
subject = sys.argv[v.tsiuriak@sentrium.io]
# read 3rd parameter, message
message = sys.argv[test]
mail_user = 'v.tsiuriak@sentrium.io'
mail_pwd = 'Headtechnology79'
# google smtp server just for example, please adjust with your smtp server address and port.
smtpserver = smtplib.SMTP("email-smtp.us-west-2.amazonaws.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(mail_user, mail_pwd)
header = 'To:' + to + '\n' + 'From: ' + mail_user + '\n' + 'Subject:'+subject+' \n'
print header
msg = header + '\n '+message+' \n\n'
smtpserver.sendmail(mail_user, to, msg)
smtpserver.close()
print 'done!'