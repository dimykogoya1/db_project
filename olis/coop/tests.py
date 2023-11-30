from django.test import TestCase
from coop.models import Institution, Address, City, Staff
from coop.importer import main as dataset

for doc in dataset():
    city = City.objects.get_or_create(name=doc['municipality'])[0]
    address = Address.objects.get_or_create(street=doc['address'], city=city, zip_code=doc['zip_code'])[0]
    library = Institution.objects.get_or_create(name=doc['institution'], code=doc['code'], address=address)
    staff = Staff.objects.get_or_create(
      name=f"{doc['first_name']} {doc['last_name']}{doc['contact']}{doc['email']}"
    )




