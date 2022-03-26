# Celery easy workkflow

## commands :

> pip install -r requirements.txt

> https://github.com/celery/celery/

> celery -A test_app.celery worker --pool=solo --loglevel=info 

> celery -A test_app.celery  worker --loglevel=info 

<br />

## Overview :
```
Getting started with celery from strach using redis as broker and postgres as backend to store task results with vanilla pythhon. Had to make to make this document because it was quite confusing .
```

### 1. Setup : Redis
```
If you are on windows :
1. Activate wsl 
2. Install any sub linux system or [Ubunut TLS](https://www.microsoft.com/store/productId/9MTTCL66CPXJ )
3. Open Linux cli follow commands :
    > sudo apt-add-repository ppa:redislabs/redis
    > suo apt-get update
    > suo apt-get upgrade
    > sudo apt-get install redis-server
    > redis-server --version
    > redis-server

4. Open another linux terminal :
    > redis-cli
    > set name nishant
    > get name

5. Redis is now ready to use

6. Optional step to view data stored :
> https://redis.io/download/#redis-stack-downloads

7. CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
```

<br />

### 2. Setup : Posgres
```
1 . Create a database in postgres 


Celery backend url systax : <database_identifier>://<postgres_username>:<password>@<hostname>/<database_name>

My local settings :
CELERY_BACKEND_URL = 'db+postgresql+psycopg2://postgres:root@localhost/celery-db'
```

<br />

### 3. Setup : Celery
```
Celery command :

1. Open a terminal in same project 
syntax  > celery -A <your_python_file>.<celery_app> worker 
        > celery -A test_app.celery_app worker --pool=solo --loglevel=info 

2. Open Another Terminal :

from task_app import factorial

>> ans = factorial.delay(10)
>> ans._get_task_meta()
>> factorial.name

```


> https://celeryproject.readthedocs.io/zh_CN/latest/userguide/tasks.html

> https://stackoverflow.com/questions/63901790/celery-how-to-get-task-name-by-task-id