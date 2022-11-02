
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_information.settings')

import django
django.setup()

from user.models import User
import random

from faker import Faker
# FAKE POP SCRIPT
fakeuser = Faker()

# def add_user():
#   t=User.objects.get_or_create(top_user=random.choice(users))[0]
#   t.save()
#   return t

def populate(N=10):
    for entry in range(N):
        # Create the fake data for that entry
        fake_first_name = fakeuser.first_name()
        fake_last_name = fakeuser.last_name()
        fake_email = fakeuser.ascii_email()
        user_rec = User.objects.get_or_create(First_Name=fake_first_name, Last_Name=fake_last_name, Email=fake_email)[0]


if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")
