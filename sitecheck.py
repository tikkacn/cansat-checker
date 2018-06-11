import requests
import html
import smtplib

def sendmail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("cansatstatuschecker@gmail.com", "cansat1234")
 
	msg = "NOT A DRILL! CanSat has been updated!"
	for address in maillist:
		server.sendmail("cansatstatuschecker@gmail.com", address, msg)
	server.quit()

maillist = ['trbinsc@gmail.com','jrd0027@uah.edu']

r = requests.get('http://www.cansatcompetition.com/mission.html')

updated = ('2019' in r.text)
if(updated):
        print('yay')
        sendmail()
else:
        print('aww')








