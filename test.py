from project.models import Library, Address, Municipality, City
from django.db import migrations

# Create list of dicts
demo_data_list = [
    {
        "library": "text1",
        "code": "code1",
        "address": "address1",
        "municipality": "municipality1",
        "city": "city1",
        "state": "state1",
        "zip_code": "zip_code1",
        "contact": "contact1",
        "phone": "phone",
        "tile": "title",
        "email": "email",
   
        
    },
    {
        "library": "text2",
        "code": "code2",
        "address": "address2",
        "municipality": "municipality2",
        "city": "city2",
        "state": "state2",
        "zip_code": "zip_code2"
    },
    {
      
    }
]

for demo in demo_data_list:
    municipality_obj, created = Municipality.objects.get_or_create(
        name=demo['municipality'],
        state=demo['state']
    )

    city_obj, created = City.objects.get_or_create(name=demo['city'])

    address, created = Address.objects.get_or_create(
        address=demo['address'],
        municipality=municipality_obj,
        city=city_obj,
        zip_code=demo['zip_code']
    )

    lib = Library.objects.filter(code=demo['code']).first()
    if not lib:
        lib = Library.objects.create(
            name=demo['library'],
            code=demo['code'],
            address=address
        )

