__author__ = 'harsimran'
# config file for Celery Daemon
from kombu import Exchange, Queue

CELERY_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
    Queue('videos',  Exchange('media'),   routing_key='media.video'),
    Queue('images',  Exchange('media'),   routing_key='media.image'),
)
CELERY_DEFAULT_QUEUE = 'default'
CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'
CELERY_DEFAULT_ROUTING_KEY = 'default'

# # default RabbitMQ broker
# BROKER_URL = 'amqp://'
#
# # default RabbitMQ backend
# CELERY_RESULT_BACKEND = 'amqp://'



BROKER_URL = 'amqp://'
CELERY_RESULT_BACKEND = 'amqp://'
C_FORCE_ROOT='true'

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_TIMEZONE = 'Europe/Oslo'
CELERY_ENABLE_UTC = True