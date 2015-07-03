__author__ = 'harsimran'
import celery


from framework.SQL.sql import update_data

result2 = update_data.apply_async(args=['new notification on kenya','{\"wheat\",\"cereal\",\"kenya\"}'],queue='notifications',routing_key='publish.notification')

# type(result2)
# update_data('dsfghj','{\"dfdhua\",\"fdsghua\"}')
