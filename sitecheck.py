import requests
import html
import smtplib
import imaplib
import re
import email

maillist = ['trb0023@uah.edu','jrd0027@uah.edu','jh0115@uah.edu','cac0049@uah.edu','jrh0056@uah.edu','dc0069@uah.edu','anj0023@uah.edu','mab0086@uah.edu','mwb0015@uah.edu','nmg0006@uah.edu']

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "cansatstatuschecker" + ORG_EMAIL
FROM_PWD    = "cansat1234"
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
	for address in maillist:
		server.sendmail(FROM_EMAIL, address, msg)
	server.quit()

def sendmail(challengetext):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(FROM_EMAIL, FROM_PWD)
 
	msg = challengetext
	server.sendmail(FROM_EMAIL, FROM_EMAIL, msg)
	server.quit()

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
			elif(isinstance(msg.get_payload()[0], str)):
				return (msg.get_payload()[0])
			else:
				return('recieve error: does not contain a string')
				
			

def cleanhtml(raw_html):
	cleanr = re.compile('<.*?>')
	cleantext = re.sub(cleanr, '', raw_html)
	return cleantext


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
	
if(excerpt != lastpage):
	sendmail(excerpt)
	sendalert(excerpt1,lastpage)


