from flask import Flask
from datetime import datetime
import requests
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    r = requests.get('http://www.cansatcompetition.com/mission.html')
    print(r.text)
    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400">

    """.format(time=the_time)+r.text

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)




