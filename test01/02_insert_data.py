import os
import psycopg2
from psycopg2.extras import Json
import urlparse
from config import config

from configparser import ConfigParser







urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse('postgres://zjppuixw:AQCCUe8DnEFRhzaUvu6WiqL3xa9BXAP0@stampy.db.elephantsql.com:5432/zjppuixw')





 
def create_tables(url):
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE vendors (
            vendor_id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(255) NOT NULL
        )
        """,
        """ CREATE TABLE parts (
                part_id SERIAL PRIMARY KEY,
                part_name VARCHAR(255) NOT NULL
                )
        """,
        """
        CREATE TABLE part_drawings (
                part_id INTEGER PRIMARY KEY,
                file_extension VARCHAR(5) NOT NULL,
                drawing_data BYTEA NOT NULL,
                FOREIGN KEY (part_id)
                REFERENCES parts (part_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE vendor_parts (
                vendor_id INTEGER NOT NULL,
                part_id INTEGER NOT NULL,
                PRIMARY KEY (vendor_id , part_id),
                FOREIGN KEY (vendor_id)
                    REFERENCES vendors (vendor_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (part_id)
                    REFERENCES parts (part_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()















def creat_table(url)
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









def insert_into_table(data):
    # preparing geometry json data for insertion
    for item in data:
        item['geom'] = Json(item['geometry'])

    with psycopg2.connect(database=url.path[1:], user=url.username, password=url.password,  host=url.hostname,  port=url.port ) as conn:
        with conn.cursor() as cursor:
            query = """
                INSERT into 
                    data_load 
                    (iso_code, l_postcode, r_postcode, link_id, geom) 
                VALUES 
                    (%(iso_code)s, %(l_postcode)s, %(r_postcode)s, %(link_id)s, st_geomfromgeojson(%(geom)s));
            """
            cursor.executemany(query, data)

        conn.commit()








# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()


