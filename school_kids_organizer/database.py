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
            'age': random.randint(0,6)
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
    with open('fakedb.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        children_list = []
        for row in reader:
            child = Child(
                first_name=row['first_name'],
                last_name=row['last_name'],
                gender=row['gender'],
                address=row['address'],
                age=int(row['age'])
            )
            children_list.append(child)
    return children_list