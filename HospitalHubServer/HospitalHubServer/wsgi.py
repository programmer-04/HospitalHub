"""
WSGI config for HospitalHubServer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
>>>>>>> 97969be225cfb49aa6da4c5e428ba1c8b9fd53dd
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HospitalHubServer.settings')

application = get_wsgi_application()
