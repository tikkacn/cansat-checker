import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")
import requests

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()



r = requests.get('http://www.cansatcompetition.com/mission.html')
print(r.text)
