from my_sqlalchemy.school.models import Group, Student, session

group = Group(name='TMS2020')
group_two = Group(name='TMS2021')

student = Student(
    firstname='Anton',
    lastname='Klimenka',
    group=group,
)
student_2 = Student(
    firstname='Konstantin',
    lastname='Toukach',
    group=group,
)
student_3 = Student(
    firstname='Maksim',
    lastname='Lamaka',
    group=group,
)

g_2_student = Student(
    firstname='Sergey',
    lastname='Klimenka',
    group=group_two,
)
g_2_student_2 = Student(
    firstname='Dmitrii',
    lastname='Toukach',
    group=group_two,
)
g_2_student_3 = Student(
    firstname='Aleksei',
    lastname='Lamaka',
    group=group_two,
)


session.add_all([group, group_two, student, student_2,
                 student_3, g_2_student, g_2_student_2, g_2_student_3])
session.commit()
