import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")
import requests
from urllib2 import Request, urlopen

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()



#request = Request('https://realemail.expeditedaddons.com/?api_key=' + os.environ['REALEMAIL_API_KEY'] + '&email=email%40example.org&fix_typos=false')

#response_body = urlopen(request).read()
#print response_body




r = requests.get('http://www.cansatcompetition.com/mission.html')
print(r.text)
