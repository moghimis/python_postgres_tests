source activate postgres
psql --host=stampy.db.elephantsql.com --port=5432 --username=zjppuixw

#password:  AQCCUe8DnEFRhzaUvu6WiqL3xa9BXAP0

#import os
#import psycopg2
#import urlparse

#urlparse.uses_netloc.append("postgres")
#url = urlparse.urlparse('postgres://zjppuixw:AQCCUe8DnEFRhzaUvu6WiqL3xa9BXAP0@stampy.db.elephantsql.com:5432/zjppuixw)
#conn = psycopg2.connect(database=url.path[1:],
#  user=url.username,
#  password=url.password,
#  host=url.hostname,
#  port=url.port
#)
