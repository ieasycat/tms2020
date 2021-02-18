"""
Получить все группы, где есть студенты с именем Антон.
"""

from my_sqlalchemy.school.models import Group, Student, session

groups_students = session.query(Group, Student).\
    join(Student, Group.id == Student.group_id).\
    filter(Student.firstname == 'Anton').all()

for gr, st in groups_students:
    print(f'{gr.id}:{gr.name}')
