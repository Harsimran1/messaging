__author__ = 'harsimran'
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pika
import json
import os
import sys
import psycopg2
from framework.celery.celery_start import celery
# import argparse



@celery.task
def update_data(notification=None,tags=None):
    con = None
    try:

        con = psycopg2.connect("host='localhost' dbname='gro' user='gro' password='gro123'")
        cur = con.cursor()
        cur.execute('SELECT version()')
        ver = cur.fetchone()
        print ver
        con.commit()
        cur.execute("INSERT INTO notifications.notification(description,tags,created_at,updated_at) VALUES(%s,%s,now(),now()) returning id",(notification,tags))
        con.commit()
        ver3=cur.fetchone()
        print ver3



        cur.execute("SELECT id from users.users WHERE subscriptions&&%s",(tags,))
        ver2=cur.fetchall()
        arr=[i[0] for i in ver2]
        print arr

        for i in arr:
            cur.execute("INSERT INTO users.user_notification(user_id,is_read,notification_id,created_at,updated_at) VALUES(%s,false,%s,now(),now()) ",(i,ver3[0]))
            con.commit()


        cur.execute("SELECT * from notifications.notification")
        ver = cur.fetchone()
        print ver
        message={
            'userids':arr
        }
        send_message(message)


    # cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
    except psycopg2.DatabaseError, e:
        print "exception",e
        sys.exit(1)


    finally:

        if con:
            con.close()

@celery.task
def send_message(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='recieveNotif',
                             type='fanout')
    # properties = pika.BasicProperties(app_id='example-publisher',
    #                                           content_type='application/json',
    #                                           headers=message)

    # message = ' '.join(sys.argv[1:]) or "info: Hello World!"
    channel.basic_publish('recieveNotif','',json.dumps(message),
                          pika.BasicProperties(content_type='application/json',
                                               delivery_mode=1)
    )
    print " [x] Sent %r" % (message,)
    connection.close()


