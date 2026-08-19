from faker import Faker
import random
fake = Faker()


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

