from sqlalchemy import create_engine

my = create_engine('sqlite:///test.db')
my.execute("""
    create table Book (
        id integer primary key,
        title varchar,
        pages int,
        author varchar,
        price float,
        release_year int
    );
""")
