__author__ = 'harsimran'
import celery

# import our send_email task
from framework.email.email_tasks import send_email
from framework.SQL.sql import update_data

# call our email function
# result = send_email.apply_async(args=['kaur.harsimran301@gmail.com', 'all your smtp  belong to us', 'somebody set up us the bomb'],queue='videos',routing_key='media.video')
result2 = update_data.apply_async(args=['new notification','{\"wheat\",\"cereal\"}'],queue='videos',routing_key='media.video')

# type(result2)
# update_data('dsfghj','{\"dfdhua\",\"fdsghua\"}')
