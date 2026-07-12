import datetime



class Child:
    """
    stores a child's data
    """
    def __init__(self, first_name: str, last_name: str, address: str, gender: str, age: datetime, group:str):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.address = address
        self.age = age
        self.group = group

    def get_child(self):
        pass

class Group:
    """
    stores group data and manages capacity limits
    """
    def __init__(self, group_name: str, min_age: datetime, max_age: datetime, limit: int):
        self.group_name = group_name
        self.min_age = min_age
        self.max_age = max_age
        self.limit = limit
        self.children = []

    def add_child(self, child: Child):
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
        self.group = []

    def take_group(self, group:Group):
        """
        Function return groups
        :param group: class Group
        :return: self.group []
        """
        self.group.append(group)

    def group_organizer(self):
        pass

child_1 = Child('Daniel','Żebrowski', 'Witosa 10', 'Male', '1', '0-3')
child_2 = Child('Adrianna','Wilczewska', 'Władysława 4', 'Female', '4', '3-6')

print(child_1.first_name, child_1.last_name, child_1.address, child_1.gender, child_1.age, child_1.group)
print(child_2.first_name, child_2.last_name, child_2.address, child_2.gender, child_2.age, child_2.group)

group_0_3 = Group(group_name='0-3', min_age=0, max_age=3, limit=12)
group_3_6 = Group(group_name='3-6', min_age=3, max_age=6, limit=22)

print(group_0_3.group_name, group_0_3.min_age, group_0_3.max_age, group_0_3.limit)
print(group_3_6.group_name, group_3_6.min_age, group_3_6.max_age, group_3_6.limit)

add_group_0_3 = Group.add_child(self=group_0_3, child=child_1)
add_group_3_6 = Group.add_child(self=group_3_6, child=child_2)


