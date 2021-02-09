CREATE TABLE User (
   id integer primary key autoincrement,
   firstname varchar(255),
   lastname varchar(255),
   age intege
);

INSERT INTO User (firstname, lastname, age) VALUES
('Anton', 'Klimenka', 28),
('Konstantin', 'Kosyak', 23),
('Dima', 'Lomako', 15),
('Diana', 'Loiko', 19),
('Roma', 'Loiko', 26);


SELECT * FROM User;

SELECT * FROM User WHERE age > 25;

SELECT * FROM User WHERE 15 <= age AND  age <= 18;