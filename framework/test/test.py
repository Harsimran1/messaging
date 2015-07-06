__author__ = 'harsimran'
import celery

from base import Notification
from framework.SQL.sql import update_data


notification= Notification(' notification description','kenya','wheat','cereal' )
result2 = update_data.apply_async(args=[notification],queue='notifications',routing_key='publish.notification')

# type(result2)
# update_data('dsfghj','{\"dfdhua\",\"fdsghua\"}')
