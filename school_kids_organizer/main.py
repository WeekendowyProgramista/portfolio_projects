from models import Child, Group, Kindergarten
from database import load_children_from_csv

kindergarten = Kindergarten()
imported_children = load_children_from_csv()

group_0_3 = Group(group_name='smoczki',min_age= 0, max_age= 3, limit= 12)
group_2_6_v1 = Group(group_name='smerfiki',min_age= 2, max_age= 6, limit= 18)
group_2_6_v2 = Group(group_name='gargamelki',min_age= 2, max_age= 6, limit= 18)
group_3_6 = Group(group_name='patyczki',min_age= 3, max_age= 6, limit= 22)

kindergarten.add_groups(group_0_3)
kindergarten.add_groups(group_2_6_v1)
kindergarten.add_groups(group_2_6_v2)
kindergarten.add_groups(group_3_6)

for child in imported_children:
    kindergarten.assign_child_to_group(child)


