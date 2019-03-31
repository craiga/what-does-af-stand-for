"""WSGI configuration"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "what_does_af_stand_for.settings")

application = get_wsgi_application()
