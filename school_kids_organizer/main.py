
"""
Tworzę grupę
↓
Dodaję jedno dziecko
↓
Wyświetlam grupę
↓
Czy dziecko jest w środku?

- usuwam def show info na rzecz __str__(...) self.children
- add_child zmieniłem na set_limit, bardziej pasuje
"""


class Child:
    """
    stores a child's data
    """
    def __init__(self, first_name: str, last_name: str, address: str, gender: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.address = address
        self.age = age

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.address}, {self.gender}, {self.age}'

class Group:
    """
    stores group data and manages capacity limits
    """
    def __init__(self, group_name: str, min_age: int, max_age: int, limit: int):
        self.group_name = group_name
        self.min_age = min_age
        self.max_age = max_age
        self.limit = limit
        self.children = []

    def __str__(self):
        return f'{self.group_name}, {self.min_age}, {self.max_age}, {self.limit}, {self.children}'

    def set_limit(self, child: Child):
        """
        Function return group limit True/False
        :param child: number of children
        :return: in or out of limit
        """
        if len(self.children) == self.limit:
            return False
        else:
            self.children.append(child)
            return True

class Kindergarden:
    """
    contains all groups, assigns children to the appropriate groups, and transfers children between groups
    """
    def __init__(self):
        self.groups = []

    def __str__(self):
        return f'All groups: {self.groups}'

    def get_groups(self, group: Group):
        return self.groups.append(group)


child_1 = Child('Daniel','Żebrowski', 'Witosa 10', 'Male', 1)
child_2 = Child('Adrianna','Wilczewska', 'Władysława 4', 'Female', 4)

group_0_3 = Group(group_name='0_3',min_age= 0, max_age= 3, limit= 12)
group_3_6 = Group(group_name='3_6',min_age= 3, max_age= 6, limit= 22)

group_0_3.set_limit(child=child_1)
group_3_6.set_limit(child=child_2)

Kindergarden().get_groups(group=group_0_3)
Kindergarden().get_groups(group=group_3_6)
print(Kindergarden())