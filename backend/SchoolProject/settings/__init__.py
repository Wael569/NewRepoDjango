"""
Django settings package.
"""
# This file makes 'settings' a Python package
# Default to dev settings
import os

env = os.environ.get('DJANGO_ENV', 'dev')

if env == 'prod':
    from .prod import *
else:
    from .dev import *