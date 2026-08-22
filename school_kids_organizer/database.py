from models import Child
from faker import Faker
import random
import csv
fake = Faker()



def fake_db():
    gender = 'male', 'female'
    kinder_list = []

    for _ in range(80):
        child = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'gender': random.choice(gender),
            'address': fake.address(),
            'age': random.randint(1,6)
        }
        kinder_list.append(child)

    return kinder_list

fake_list = fake_db()


with open('fakedb.csv', 'w', newline='') as csv_file:
    fieldnames = ['first_name', 'last_name', 'gender', 'address', 'age']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for child in fake_list:
        writer.writerow(child)


def load_children_from_csv():

