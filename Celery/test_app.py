from random import randrange
from celery import Celery
from celery import shared_task

# CELERY_BROKER_URL = 'amqp://myuser:mypassword@localhost/myvhost'
# CELERY_BACKEND_URL = 'db+sqlite:///test.db'


CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_BACKEND_URL = 'db+postgresql+psycopg2://postgres:root@localhost/celery-db'

celery_app = Celery(
    main = 'CELERY_TEST_APP',
    backend= CELERY_BACKEND_URL,
    broker= CELERY_BROKER_URL,
    result_extended = True
)


@celery_app.task(name= 'factorial')
def factorial(n):
    if n <= 1:
        return n

    fact = 1
    for i in range(n):
        fact *= i
    return fact


@shared_task()
def add(x, y):
    return x + y