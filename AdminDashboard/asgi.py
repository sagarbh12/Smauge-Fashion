"""
<<<<<<< HEAD
ASGI config for Smaugefashionhub project.
=======
ASGI config for Ranashreecollection project.
>>>>>>> 778d59a5e089a051b0abcb73d9fb62538c39e154

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<< HEAD
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Smaugefashionhub.settings")
=======
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Ranashreecollection.settings")
>>>>>>> 778d59a5e089a051b0abcb73d9fb62538c39e154

application = get_asgi_application()
