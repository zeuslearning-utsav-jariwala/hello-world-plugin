"""
hello_world Django application initialization.
"""

from django.apps import AppConfig


class HelloWorldConfig(AppConfig):
    """
    Configuration for the hello_world Django application.
    """

    name = 'hello_world'
    domain_name = 'hello_world'
    verbose_name = 'hello world plugin'
    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': name,
                'regex': f'^{name}/',
                'relative_path': 'urls',
            },
        },
        'settings_config': {
            'lms.djangoapp': {
                'production': {'relative_path': 'test_settings'},
                'common': {'relative_path': 'test_settings'},
                'devstack': {'relative_path': 'test_settings'},
            },
        },
    }
