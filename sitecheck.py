import requests
import html
import smtplib

maillist = ['trbinsc@gmail.com','jrd0023@uah.edu']

r = requests.get('http://www.cansatcompetition.com/mission.html')

updated = ('2019' in r.text)
if(updated):
        print('yay')
else:
        print('aww')

sendmail()

def sendmail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("cansatstatuschecker@gmail.com", "cansat1234")
 
	msg = "(Just a drill) CanSat has been Updated!"
	for address in maillist:
		server.sendmail("cansatstatuschecker@gmail.com", address, msg)
	server.quit()




