import os
import sys
from datetime import datetime
from pathlib import Path

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 200

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USE_TZ = False

django.setup()
import faker
from django.contrib.auth.models import User
if __name__ == '__main__':
    

    from contact.models import  Contact

    Contact.objects.all().delete()

    fake = faker.Faker('pt_BR')

    django_contacts = []

    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        email = profile['mail']
        first_name, last_name = profile['name'].split(' ', 1)
        phone = fake.phone_number()
        created_date: datetime = fake.date_this_year()
        description = fake.text(max_nb_chars=100)
        owner = User.objects.first()
        django_contacts.append(
            Contact(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                created_date=created_date,
                description=description,
                owner=owner,
            )
        )

    if len(django_contacts) > 0:
        Contact.objects.bulk_create(django_contacts)
