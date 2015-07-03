__author__ = 'harsimran'
import celery

from framework.email.email_tasks import send_email
from framework.SQL.sql import update_data

result2 = update_data.apply_async(args=['new notification','{\"wheat\",\"cereal\"}'],queue='videos',routing_key='media.video')

