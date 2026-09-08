from models import Child, Group, Kindergarten
from database import load_children_from_csv

"""
Main entry point for the Kindergarten Management System.

This script initializes core domain models, imports child records 
from a temporary CSV data source, configures group capacities and age rules, 
and executes a load-balancing algorithm to assign children to groups.

Note:
    Currently relies on CSV file parsing for persistence. A full database 
    migration to PostgreSQL is planned for production readiness.
"""

def main():
    """Executes the primary workflow for importing and assigning children to groups."""
    kindergarten = Kindergarten()
    imported_children = load_children_from_csv()

    group_0_3 = Group(group_name='FROGS',min_age= 0, max_age= 3, limit= 12)
    group_2_6_v1 = Group(group_name='BEARS',min_age= 2, max_age= 6, limit= 18)
    group_2_6_v2 = Group(group_name='FOXES',min_age= 2, max_age= 6, limit= 18)
    group_3_6 = Group(group_name='OWLS',min_age= 3, max_age= 6, limit= 22)

    kindergarten.add_groups(group_0_3)
    kindergarten.add_groups(group_2_6_v1)
    kindergarten.add_groups(group_2_6_v2)
    kindergarten.add_groups(group_3_6)

    # Sort children deterministically by age (ascending) and gender to ensure
    # fair demographic distribution during assignment
    sorted_children = sorted(imported_children, key=lambda c:(c.age, c.gender))

    # Iterate through sorted children and assign each to the optimal group
    for child in sorted_children:
        kindergarten.assign_child_to_group(child)


if __name__== '__main__':
    main()