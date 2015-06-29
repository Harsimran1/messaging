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
       print ver3



       cur.execute("SELECT id from users.users WHERE subscriptions&&%s",(tags,))
       ver2=cur.fetchall()
       arr=[i[0] for i in ver2]
       print arr

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

# update_data('dsfghj','{\"africa\",\"cereal\"}')

# db_conn_str = "dbname=regress user=craig"
#
# create_table_stm = """
# CREATE TABLE files (
#     id serial primary key,
#     orig_filename text not null,
#     file_data bytea not null
# )
# """
#
# def main(argv):
#     parser = argparse.ArgumentParser()
#     parser_action = parser.add_mutually_exclusive_group(required=True)
#     parser_action.add_argument("--store", action='store_const', const=True, help="Load an image from the named file and save it in the DB")
#     parser_action.add_argument("--fetch", type=int, help="Fetch an image from the DB and store it in the named file, overwriting it if it exists. Takes the database file identifier as an argument.", metavar='42')
#     parser.add_argument("filename", help="Name of file to write to / fetch from")
#
#     args = parser.parse_args(argv[1:])
#
#     conn = psycopg2.connect(db_conn_str)
#     curs = conn.cursor()
#
#     # Ensure DB structure is present
#     curs.execute("SELECT 1 FROM information_schema.tables WHERE table_schema = %s AND table_name = %s", ('public','files'))
#     result = curs.fetchall()
#     if len(result) == 0:
#         curs.execute(create_table_stm)
#
#     # and run the command
#     if args.store:
#         # Reads the whole file into memory. If you want to avoid that,
#         # use large object storage instead of bytea; see the psycopg2
#         # and postgresql documentation.
#         f = open(args.filename,'rb')
#
#         # The following code works as-is in Python 3.
#         #
#         # In Python 2, you can't just pass a 'str' directly, as psycopg2
#         # will think it's an encoded text string, not raw bytes. You must
#         # either use psycopg2.Binary to wrap it, or load the data into a
#         # "bytearray" object.
#         #
#         # so either:
#         #
#         #   filedata = psycopg2.Binary( f.read() )
#         #
#         # or
#         #
#         #   filedata = buffer( f.read() )
#         #
#         filedata = f.read()
#         curs.execute("INSERT INTO files(id, orig_filename, file_data) VALUES (DEFAULT,%s,%s) RETURNING id", (args.filename, filedata))
#         returned_id = curs.fetchone()[0]
#         f.close()
#         conn.commit()
#         print("Stored {0} into DB record {1}".format(args.filename, returned_id))
#
#     elif args.fetch is not None:
#         # Fetches the file from the DB into memory then writes it out.
#         # Same as for store, to avoid that use a large object.
#         f = open(args.filename,'wb')
#         curs.execute("SELECT file_data, orig_filename FROM files WHERE id = %s", (int(args.fetch),))
#         (file_data, orig_filename) = curs.fetchone()
#
#         # In Python 3 this code works as-is.
#         # In Python 2, you must get the str from the returned buffer object.
#         f.write(file_data)
#         f.close()
#         print("Fetched {0} into file {1}; original filename was {2}".format(args.fetch, args.filename, orig_filename))
#
#     conn.close()
#
# if __name__ == '__main__':
#     main(sys.argv)
