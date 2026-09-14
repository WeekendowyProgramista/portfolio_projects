from faker import Faker
import random
from datetime import date
import csv
fake = Faker()

"""
	child(
	child_id serial primary key,
	first_name varchar(100),
	last_name varchar(25),
	gender varchar(10) check (gender in ('male', 'female')),
	birth_date date ,
	street varchar(100),
	house_number varchar(25),
	postal_code varchar(25),
	city varchar (100),
	group_id int,
	contact_person VARCHAR(100),
    contact_number VARCHAR(20),
    created_at timestamp with time zone default current_timestamp
"""



def fake_db():
    """
    Generates a dataset of mock child profiles with randomized demographic data.
    """
    gender = 'male', 'female'
    kinder_list = []

    for _ in range(78):
        child = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'gender': random.choice(gender),
            'birth_date': fake.date_between(start_date=date (2020,1,1), end_date=date(2026,12,31)),
            'street': fake.street_name(),
            'house_number': fake.building_number(),
            'postal_code': fake.postcode(),
            'city': fake.city(),
            'group_id': None,
            'contact_person': fake.name(),
            'contact_number': fake.phone_number()



        }
        kinder_list.append(child)

    return kinder_list

fake_list = fake_db()
# for index,fake in enumerate(fake_list):
#     print(index, fake)

# Export the mock dataset to a CSV file with standardized column headers.

with open('../data/fakedb.csv', 'w', newline='') as csv_file:
    fieldnames = ['first_name', 'last_name', 'gender', 'birth_date', 'street', 'house_number', 'postal_code', 'city', 'group_id', 'contact_person', 'contact_number']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for child in fake_list:
        writer.writerow(child)


# def load_children_from_csv():
#     """
#     Imports child data from 'fakedb.csv' and returns a list of Child instances.
#     """
#     with open('fakedb.csv', 'r', newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         children_list = []
#         for row in reader:
#             child = Child(
#                 first_name=row['first_name'],
#                 last_name=row['last_name'],
#                 gender=row['gender'],
#                 address=row['address'],
#                 age=int(row['age'])
#             )
#             children_list.append(child)
#     return children_list