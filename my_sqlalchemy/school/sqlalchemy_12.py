from my_sqlalchemy.school.models import Student, Diary, session

students = session.query(Student).all()
for student in students:
    print(student)

diary = Diary(average_score=8, student_id=1)
diary_2 = Diary(average_score=9, student_id=2)
diary_3 = Diary(average_score=7, student_id=3)
diary_4 = Diary(average_score=6, student_id=4)
diary_5 = Diary(average_score=9, student_id=5)
diary_6 = Diary(average_score=8, student_id=6)

session.add_all([diary, diary_2, diary_3, diary_4, diary_5, diary_6])
session.commit()

pr_diarys = session.query(Diary).all()
for pr_diary in pr_diarys:
    print(pr_diary)
