- pip3 install psycopg2
- pip3 install sqlalchemy
- pip3 install "passlib[bcrypt]"
- pip3 install "python-jose[cryptography]"
- pip3 install alembic

- pip3 install -r requirements.txt

psql -h localhost -p 5432 -U postgres -d fastapi


```
fastapi=# \d+ posts
                                                                  Table "public.posts"
   Column   |           Type           | Collation | Nullable |              Default              | Storage  | Compression | Stats target | Description 
------------+--------------------------+-----------+----------+-----------------------------------+----------+-------------+--------------+-------------
 id         | integer                  |           | not null | nextval('posts_id_seq'::regclass) | plain    |             |              | 
 title      | character varying        |           | not null |                                   | extended |             |              | 
 details    | character varying        |           | not null |                                   | extended |             |              | 
 published  | boolean                  |           | not null | true                              | plain    |             |              | 
 created_at | timestamp with time zone |           | not null | now()                             | plain    |             |              | 
 owner_id   | integer                  |           | not null |                                   | plain    |             |              | 
Indexes:
    "posts_pkey" PRIMARY KEY, btree (id)
Foreign-key constraints:
    "posts_owner_id_fkey" FOREIGN KEY (owner_id) REFERENCES users(id) ON DELETE CASCADE
Access method: heap

fastapi=# 
```

Alembic Tool
- DB migrations/ changes to database
- can automatically pull databases from sqlqlchemy and generate proper tables
- alembic init alembic
- make changes to env.py and alembic.ini files
- drop existing tables
```
psql -h localhost -p 5432 -U postgres -d fastapi

fastapi=# drop table votes
fastapi-# ;
DROP TABLE
fastapi=# drop table users;
ERROR:  cannot drop table users because other objects depend on it
DETAIL:  constraint posts_owner_id_fkey on table posts depends on table users
HINT:  Use DROP ... CASCADE to drop the dependent objects too.
fastapi=# drop table users CASCADE;
NOTICE:  drop cascades to constraint posts_owner_id_fkey on table posts
DROP TABLE
fastapi=# drop table posts CASCADE;
DROP TABLE
fastapi=# 

```
- alembic revision -m "create posts table"
- configure alembic/versions/py file
```
(venv) snehanshu.suman@LT7818 authentication % alembic current
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
(venv) snehanshu.suman@LT7818 authentication % 

(venv) snehanshu.suman@LT7818 authentication % alembic upgrade d09650249ab1  
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
(venv) snehanshu.suman@LT7818 authentication %



```
