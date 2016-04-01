"""
WSGI config for ImpaQto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys

sys.path.append('/opt/ImpaQto')
sys.path.append('/usr/local/lib/python3.5/site-packages')
sys.path.append('/opt/ImpaQto/static')



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ImpaQto.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
