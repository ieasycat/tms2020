CREATE TABLE Book (
	id integer,
	title varchar,
	pages int,
	author varchar,
	price float
);


ALTER TABLE Book ADD COLUMN release_year int;
