import datetime
from tokenize import group


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

    def add_group(self):
        pass

