"""
WSGI config for Gonghangguize project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Gonghangguize.settingss")

#新修改的
# profile = os.environ.get('TYPEIDEA_PROFILE',)
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Gonghangguize.settingss.%s' % profile)

application = get_wsgi_application()
