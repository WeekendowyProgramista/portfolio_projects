
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

    __repr__ = __str__


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

    def add_child(self, child: Child):
        """
        Adds a child to the group's roster if space is available.
        """
        if len(self.children) == self.limit:
            return False
        else:
            self.children.append(child)
            return True

class Kindergarten:
    """
    contains all groups, assigns children to the appropriate groups, and transfers children between groups
    """
    def __init__(self):
        self.all_children = []
        self.all_groups = []

    def __str__(self):
        groups = []
        for group in self.all_groups:
            groups.append(str(group))
        groups_final = '\n'.join(groups)

        children = []
        for child in self.all_children:
            children.append(str(child))
        children_final = '\n'.join(children)

        return f'{children_final}\n{groups_final}'

    def add_groups(self, group: Group):
        """
        Adds a group instance to the kindergarten's internal list of groups.
        """
        self.all_groups.append(group)

    def add_children(self, child: Child):
        """
        Adds a child instance to the kindergarten's master list of registered children.
        """
        self.all_children.append(child)

    def assign_child_to_group(self, child):
        """
        Assigns a child to the least populated matching group that satisfies age and capacity limits.
        """
        matching_groups = []

        for group in self.all_groups:
            if group.min_age <= child.age < group.max_age and len(group.children) < group.limit:
                matching_groups.append(group)
        if not matching_groups:
            return False

        best_group = min(matching_groups, key=lambda g: len(g.children))
        best_group.children.append(child)
        return True



