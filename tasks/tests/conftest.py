import os
import django
from django.conf import settings

def pytest_configure():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pydjango_ci_integration.settings')
    django.setup()