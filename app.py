from flask import Flask
from datetime import datetime
import requests
from difflib import *
import html
import smtplib
app = Flask(__name__)

maillist = ['trbinsc@gmail.com','jrd0023@uah.edu']

@app.route('/')
def homepage():
	the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

	r = requests.get('http://www.cansatcompetition.com/mission.html')

	updated = ('2019' in r.text)
	if(updated):
		print('yay')
		
		checkvar = '</p><h2>HAS BEEN UPLOADED!</h2>'
	else:
		print('aww')
		checkvar = 'has not been uploaded.</p>'

	sendmail()

	return """
	<h1>Hello Obsessed CanSatters!</h1>
	<p>It is currently {time}.</p>
	<p>The 2019 CanSat Mission {check}


	<img src="http://loremflickr.com/600/400">

	""".format(time=the_time, check = checkvar)

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)

def sendmail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("cansatstatuschecker@gmail.com", "cansat1234")
 
	msg = "(Just a drill) CanSat has been Updated!"
	for address in maillist:
		server.sendmail("cansatstatuschecker@gmail.com", address, msg)
	server.quit()




