import os
import sys
path = '/srv/www/shopping-webapp/shopping'
if path not in sys.path:
   sys.path.insert(0, '/srv/www/shopping-webapp/shopping')

os.environ['DJANGO_SETTINGS_MODULE'] = 'shopping.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
