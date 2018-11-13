#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import psycopg2
import psycopg2.extras
import psycopg2.extensions

DB_HOST = os.environ.get('DATABASE_HOST', '')
DB_PORT = os.environ.get('DATABASE_PORT', '')
DB_USER = os.environ.get('DATABASE_USER', '')
DB_PASSWORD = os.environ.get('DATABASE_PASSWORD', '')
DB_NAME = os.environ.get('DATABASE_NAME', '')
DB_SYS_DATABASE = 'postgres'

con = None
try:
  con = psycopg2.connect(
    user=DB_USER,
    host = DB_HOST,
    port = DB_PORT,
    password=DB_PASSWORD,
    dbname=DB_SYS_DATABASE
    )
  con.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

  cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
  cur.execute("select * from pg_database where datname = %(dname)s", {'dname': DB_NAME })
  answer = cur.fetchall()
  if len(answer) > 0:
    print("Database {} already exists".format(DB_NAME))
  else:
    print("Database {} does NOT exist".format(DB_NAME))
    cur = con.cursor()
    cur.execute('CREATE DATABASE ' + DB_NAME)
    cur.close()
    print("Created database {}".format(DB_NAME))

except Exception as e:
  print("Error %s" %e)
  sys.exit(1)
finally:
  if con:
    con.close()
