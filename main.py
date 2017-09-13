# Django specific settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Your application specific imports
# from kobis.models import User
from kobis.models import (
    Boxoffice,
    Movies,
)


#Add user
# user = User(name="masnun", email="masnun@gmail.com")
# user.save()

# Application logic
# first_user = User.objects.all()[0]
b = Boxoffice.objects.all()

# print(first_user.name)
# print(first_user.email)
print(b)
