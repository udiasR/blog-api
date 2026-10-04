import os
from settings.conf import ENV_ID

from django.core.wsgi import get_wsgi_application

assert ENV_ID, "Environmental value is not"

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'settings.env{ENV_ID}')

application = get_wsgi_application()
