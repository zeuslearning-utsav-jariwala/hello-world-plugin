"""
Common Django settings for openedx_lti_tool_plugin project.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
from django.conf import LazySettings

INSTALLED_APPS = []
ROOT_URLCONF = 'hello_world.urls'

MIDDLEWARE = (
    'django.contrib.contenttypes',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ALLOWED_HOSTS = ["*"]