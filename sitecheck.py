import os
import requests
import html
import smtplib
import imaplib
import re
import email
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import random
import datetime


maillist = ['trb0023@uah.edu','jrd0027@uah.edu','jh0115@uah.edu','cac0049@uah.edu','jrh0056@uah.edu','dc0069@uah.edu','anj0023@uah.edu','mab0086@uah.edu','mwb0015@uah.edu','nmg0006@uah.edu','cd0040@uah.edu','ajb0042@uah.edu','fj0009@uah.edu']
catlist = ['trb0023@uah.edu','jrd0027@uah.edu','jh0115@uah.edu','cac0049@uah.edu','jrh0056@uah.edu','dc0069@uah.edu','anj0023@uah.edu','mab0086@uah.edu','nmg0006@uah.edu','cd0040@uah.edu','ajb0042@uah.edu','fj0009@uah.edu']


ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "cansatstatuschecker" + ORG_EMAIL
FROM_PWD = os.environ['EMAIL_PWD']
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

def sendalert(challengetext = "", oldtext = ""):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(FROM_EMAIL, FROM_PWD)
 
	msg = "CanSat has been updated! This is not a drill! \nnew: "+challengetext+"\nold: "+oldtext
	for address in maillist:
		server.sendmail(FROM_EMAIL, address, msg)
	server.quit()

def senderror(challengetext = ""):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(FROM_EMAIL, FROM_PWD)
 
	msg = "Cansat Checker Error \n"+challengetext
	server.sendmail(FROM_EMAIL, "trb0023@uah.edu", msg)
	server.quit()

def sendmail(challengetext):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(FROM_EMAIL, FROM_PWD)
 
	msg = challengetext
	server.sendmail(FROM_EMAIL, FROM_EMAIL, msg)
	server.quit()

def sendcats():
	msg = MIMEMultipart()
	msg['Subject'] = 'Herb\'s Cat Picture #'+str(random.randint(1000,9999))
	msg['From'] = FROM_EMAIL
	msg['To'] = ', '.join(catlist)

	response = requests.get('http://loremflickr.com/600/400')

	text = MIMEText("""The CanSat Status Checker is still working! Now with less false alarms when people email this address! (Looking at you Herb)\n\nHere's some cats for Herb: \n
<img src="{imglink}"> \n if you don't want to get the daily cat pictures but still want CanSat updates, let me know at trb0023@uah.edu""".format(imglink = response.url),'html')
	msg.attach(text)

	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.ehlo()
	s.starttls()
	s.ehlo()
	s.login(FROM_EMAIL, FROM_PWD)
	for address in catlist:
		s.sendmail(FROM_EMAIL, address, msg.as_string())
	s.quit()

def readmail():
	mail = imaplib.IMAP4_SSL(SMTP_SERVER)
	mail.login(FROM_EMAIL,FROM_PWD)
	mail.select('inbox')
	type, data = mail.search(None, 'ALL')
	mail_ids = data[0]
	id_list = mail_ids.split()
	
	typ, data = mail.fetch(id_list[-1], '(RFC822)' )

	for response_part in data:
		if isinstance(response_part, tuple):
			msg = email.message_from_string(response_part[1].decode('utf-8'))
			mail.close()
			if isinstance(msg.get_payload(), str):
				return (msg.get_payload())
			else:
				return('recieve error, does not contain a string')
				
			

def cleanhtml(raw_html):
	cleanr = re.compile('<.*?>')
	cleantext = re.sub(cleanr, '', raw_html)
	return cleantext


print(str(datetime.datetime.now().hour)+':'+str(datetime.datetime.now().minute))
if(datetime.datetime.now().hour == 17 and datetime.datetime.now().minute < 10):
	print('sending cats')
	sendcats()

try:
	r = requests.get('http://www.cansatcompetition.com/mission.html')

	excerpt1 = cleanhtml(r.text.partition("<h2>Documents</h2>")[2].partition('<div id="scroll">')[0])
	excerpt = excerpt1.strip()
	excerpt = excerpt.replace('\n', '').replace('\r', '').replace(': ',':')
	print(excerpt)
	print('\n')

	lastpage = readmail().replace('\n', '').replace('\r', '').replace(': ',':')
	print(lastpage)

except:
	senderror()
	lastpage = ''

if(lastpage == 'recieve error, does not contain a string'):
	senderror()
	sendmail(excerpt)
elif(excerpt != lastpage):
	sendmail(excerpt)
	sendalert(excerpt1,lastpage)


