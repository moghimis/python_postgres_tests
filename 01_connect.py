#!/usr/bin/python
import psycopg2
from config import config
 
def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
 
        # create a cursor
        cur = conn.cursor()
        
 # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
 
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
     # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
 
 
if __name__ == '__main__':
    connect()


"""
conn = psycopg2.connect(database=url.path[1:],
  user=url.username,
  password=url.password,
  host=url.hostname,
  port=url.port
)




 a cursor to perform database operations
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

"""
