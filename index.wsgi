import os
import sys
app_root = os.path.dirname(__file__)
sys.path.insert(0,os.path.join(app_root,'site-packages'))

#import django.core.handlers.wsgi

import sae

os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'

#application = sae.create_wsgi_app(django.core.handlers.wsgi.WSGIHandler())

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()