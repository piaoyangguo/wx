import os
import sys

root = os.path.dirname(__file__)

sys.path.insert(0, os.path.join(root, 'site-packages'))
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
