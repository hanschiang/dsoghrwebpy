# reference

# sqlite3 for web.py
https://kzar.co.uk/blog/2009/07/10/web.py-tutorial-sqlite/

# 1. create table by sqlite3

create table todo (
    id integer primary key, 
    title text, 
    created datetime default (strftime('%s', 'now')), 
    done boolean default 'f'
); 


# 2. create an entry with this SQL

insert into todo (title) values ('Learn web.py');



# Check Column Names of a Table

.header on
.mode colum
pragma table_info(table_name);



# empty database

DELETE FROM table_name;