from psycopg2 import connect
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import settings
#def createDB()
con = None
con = connect(user = settings.USER, host = settings.HOST, password = settings.PASSSWORD)

dbname = settings.DB_NAME

con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = con.cursor()
cur.execute('CREATE DATABASE ' + dbname)
cur.close()
con.close()