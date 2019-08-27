"""
WSGI config for profiles_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'profiles_project.settings')
<<<<<<< HEAD
=======
os.environ['HTTPS'] = "on"

>>>>>>> cbaa36b75dfb4201313cb3465590d418cc32ef64
application = get_wsgi_application()
