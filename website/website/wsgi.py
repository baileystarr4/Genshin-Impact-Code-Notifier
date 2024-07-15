
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '.settings')

application = get_wsgi_application()

# Connect to Django app on Vercel
app = application
