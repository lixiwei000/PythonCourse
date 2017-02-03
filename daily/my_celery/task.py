from celery import Celery
import time

celery = Celery('tasks', broker='redis://localhost:6379/5')

@celery.task
def sendmail(mail):
    print('sending mail to %s...' % mail['to'])
    time.sleep(2.0)
    print('mail sent.')