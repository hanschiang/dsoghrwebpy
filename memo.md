# reference

# sqlite3 for web.py
https://kzar.co.uk/blog/2009/07/10/web.py-tutorial-sqlite/

# 1. create table by sqlite3

參考網站的寫法：
create table todo (
    id integer primary key, 
    title text, 
    created datetime default (strftime('%s', 'now')), 
    done boolean default 'f'
); 


改本地時間，改時間格式：
create table todo2 (
    id integer primary key, 
    title text, 
    created datetime default (strftime('%Y/%m/%d %H:%M:%S', 'now', 'localtime')), 
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