from my_sqlalchemy.book import Books, session


book_1 = Books('Harry Potter', 999, 'Diana', 790.99, 2008)
book_2 = Books('Harry Potter 2', 850, 'Diana', 749.33, 2010)
book_3 = Books('Harry Potter 3', 897, 'Diana', 767, 2012)
session.add_all([book_1, book_2, book_3])
session.commit()
