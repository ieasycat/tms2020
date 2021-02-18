from my_sqlalchemy.school.models import Student, Diary, session
from random import randint

students = session.query(Student).all()
for student in students:
    print(student)
    diary = Diary(average_score=(randint(4, 9)), student=student)
    session.add(diary)
session.commit()
