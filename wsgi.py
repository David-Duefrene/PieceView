"""
WSGI config for PieceView project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/

### urls.py
### Copyright 2019 David J Duefrene, All rights reserved.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PieceView.settings')

application = get_wsgi_application()
