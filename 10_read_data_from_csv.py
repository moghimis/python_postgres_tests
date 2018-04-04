#!/usr/bin/python
import psycopg2
from config import config
import csv
"""
Not working so far

"""

def read_from_csv(path_to_file):
    """ insert a csv into a table """
    
    conn = None
    try:
        # read data from a picture
        part_list = open(path_to_file, 'r')  #.read()
        # read database configuration
        params = config()
        # connect to the PostgresQL database
        conn = psycopg2.connect(**params)
        # create a new cursor object
        cur = conn.cursor()
        
        
        
        
        
        
        
        
        #with open(path_to_file, 'r') as f:
        #    next (f) #skip headre
        #    cur.copy_from(f, 'parts', sep=',')
        
        cur.copy_from(part_list, 'parts', sep=',')
        
        # commit the changes to the database
        conn.commit()
        # close the communication with the PostgresQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()




def read_from_csv_vendors(path_to_file):
    """ insert a csv into a table """
    
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgresQL database
        conn = psycopg2.connect(**params)
        # create a new cursor object
        cur = conn.cursor()

        with open(path_to_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header row.
            for row in reader:
                cur.execute(
                    "INSERT INTO vendors VALUES (%s, %s)",
                    row
                )
        conn.commit()
        # close the communication with the PostgresQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()




def read_from_csv_users(path_to_file):
    """ insert a csv into a table """
    
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgresQL database
        conn = psycopg2.connect(**params)
        # create a new cursor object
        cur = conn.cursor()

        #f = open(path_to_file, 'r')
        #cur.copy_from(f, 'users', sep=',')
        
                
        with open(path_to_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header row.
            for row in reader:
                cur.execute(
                    "INSERT INTO users VALUES (%s, %s, %s, %s)",
                    row
                )
                
        
        f.close()
        conn.commit()
        # close the communication with the PostgresQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':

    # read database configuration
    params = config()
    # connect to the PostgresQL database
    conn = psycopg2.connect(**params)
    # create a new cursor object
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE users(
        id integer PRIMARY KEY,
        email text,
        name text,
        address text
    )
    """)
    conn.commit()
    # close the communication with the PostgresQL database
    cur.close()


    #read_from_csv         (path_to_file='parts.csv')
    #read_from_csv_users (path_to_file='vendors.csv')    
    read_from_csv_users (path_to_file='users.csv')    

