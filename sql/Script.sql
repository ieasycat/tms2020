CREATE TABLE Book (
	id integer,
	title varchar,
	pages int,
	author varchar,
	price float
);


ALTER TABLE Book ADD COLUMN release_year int;


INSERT INTO Book (id, title, pages, author, price, release_year) VALUES 
(2, 'Harry Potter', 999, 'Diana', 750.79, 2008),
(3, 'Harry Potter 2', 807, 'Diana', 730.00, 2010),
(4, 'Harry Potter 3', 799, 'Diana', 700.19, 2012),
(5, 'Harry Potter 4', 809, 'Diana', 725.09, 2014),
(6, 'Harry Potter 5', 909, 'Diana', 745.99, 2016);


SELECT release_year, title, price FROM Book;

SELECT release_year, title, price FROM Book WHERE release_year = 2010;