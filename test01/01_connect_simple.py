import os
import psycopg2
import urlparse

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse('postgres://zjppuixw:AQCCUe8DnEFRhzaUvu6WiqL3xa9BXAP0@stampy.db.elephantsql.com:5432/zjppuixw)
conn = psycopg2.connect(database=url.path[1:],
  user=url.username,
  password=url.password,
  host=url.hostname,
  port=url.port
)

# Open a cursor to perform database operations
cur = conn.cursor()


# Execute a command: this creates a new table
cur.execute("CREATE TABLE test3 (id serial PRIMARY KEY, num integer, data varchar);")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
cur.execute("INSERT INTO test3 (num, data) VALUES (%s, %s)",(100, "abc'def"))
cur.execute("INSERT INTO test3 (num, data) VALUES (%s, %s)",(200, "sjkhdgs"))
cur.execute("INSERT INTO test3 (num, data) VALUES (%s, %s)",(500, "xxxhdgs"))

# Query the database and obtain data as Python objects
cur.execute("SELECT * FROM test3;")
cur.fetchall()



# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()


