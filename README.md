- pip3 install psycopg2
- pip3 install sqlalchemy
- pip3 install "passlib[bcrypt]"
- pip3 install "python-jose[cryptography]"
- pip3 install alembic

- python3 --version
- python3  -m venv venv
- source venv/bin/activate 

- sudo python3 -m ensurepip --upgrade
- sudo yum install postgresql-devel
- sudo yum groupinstall 'Development Tools'
- sudo yum install python3-devel
- sudo pip3 install --upgrade awscli
- sudo pip3 install -r requirements.txt
- sudo uvicorn app.main:app --host 0.0.0.0 --port 80 &
- sudo uvicorn app.main:app --host 0.0.0.0 --port 80 --forwarded-allow-ips '*' &
  https://stackoverflow.com/questions/63511413/fastapi-redirection-for-trailing-slash-returns-non-ssl-link
- uvicorn app.main:app --reload
- python3 -m ensurepip --upgrade
- 


- psql -h localhost -p 5432 -U postgres -d fastapi
- sudo yum install postgresql15


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
```
(venv) snehanshu.suman@LT7818 posts-api % pip3 install -t dependencies -r requirements.txt
(venv) snehanshu.suman@LT7818 posts-api % cd dependencies
(venv) snehanshu.suman@LT7818 posts-api % zip ../aws_lambda_artifact.zip -r .                                                                        
(venv) snehanshu.suman@LT7818 dependencies % cd ..
(venv) snehanshu.suman@LT7818 posts-api % zip -g ./aws_lambda_artifact.zip -r app -x "app/venv*" -x "app/__pycache__*" -x "app/routers/__pycache__*"

  adding: app/ (stored 0%)
  adding: app/routers/ (stored 0%)
  adding: app/routers/auth.py (deflated 52%)
  adding: app/routers/post.py (deflated 73%)
  adding: app/routers/user.py (deflated 51%)
  adding: app/routers/health.py (deflated 15%)
  adding: app/routers/vote.py (deflated 60%)
  adding: app/config.py (deflated 49%)
  adding: app/models.py (deflated 66%)
  adding: app/oauth2.py (deflated 55%)
  adding: app/database.py (deflated 51%)
  adding: app/__init__.py (stored 0%)
  adding: app/schemas.py (deflated 65%)
  adding: app/utils.py (deflated 47%)
  adding: app/main.py (deflated 54%)
(venv) snehanshu.suman@LT7818 posts-api % zip -g ./aws_lambda_artifact.zip -r .env       
```