__author__ = 'harsimran'
#!/usr/bin/python3
# -*- coding: utf-8 -*-

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
       cur.execute("INSERT INTO notifications.notification(description,tags,created_time) VALUES(%s,%s,now()) returning id",(notification,tags))
       con.commit()
       ver3=cur.fetchone()
       
       cur.execute("SELECT id from users.users WHERE subscriptions&&%s",(tags,))
       ver2=cur.fetchall()
       arr=[i[0] for i in ver2]
       
       for i in arr:
           cur.execute("INSERT INTO users.user_notifications(user_id,is_read,notification_id) VALUES(%s,false,%s) ",(i,ver3[0]))
           con.commit()


       cur.execute("SELECT * from notifications.notification")
       ver = cur.fetchone()
       print ver

    # cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
    except psycopg2.DatabaseError, e:
       print "exception",e
       sys.exit(1)


    finally:

       if con:
        con.close()

