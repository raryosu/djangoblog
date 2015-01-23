"""
WSGI config for raryosublog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import site
import sys

# Virtualenv
site.addsitedir("/home/raryosu/ENV/lib/python3.3/site-packages")

sys.path.append('/var/www/cgi-bin/raryosublog')
sys.path.append('/var/www/cgi-bin/raryosublog/raryosublog')

os.environ['DJANGO_SETTINGS_MODULE'] = 'raryosublog.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "raryosublog.settings")

active_env = os.path.expanduser("/home/raryosu/ENV/bin/active_this.py")
execfile(active_env, dict(__file__=active_env))


#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
