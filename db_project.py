
# Load the postgres module
import psycopg2

# Create a connection object
con = psycopg2.connect(database="my_db", user="postgres", password="postgres", host="127.0.0.1", port="5432")

#table name
TABLE_NAME = "us_users"
# Create a cursor via the connection
cur = con.cursor()
cur.execute(f"drop table if exists {TABLE_NAME}")
cur.execute(""" CREATE TABLE us_users(

    first_name text not null,
    last_name text not null,
    address text not null,
    city text,
    country text,
    state text,
    zip text,
    phone1 text,
    phone2 text
)  
""")

with open('us-users.csv','r') as f:
    next(f)
    cur.copy_from(f,'us_users',sep=',')

f.close()

#Adding an auto increment id to the table
cur.execute(f"alter table {TABLE_NAME} add user_id SERIAL primary key ")

#committing changes
con.commit()

# Query via the cursor
cur.execute("select * from us_users")

#fetching rows in db
rows = cur.fetchall()
for row in rows:
    print(row)



#close cursor
cur.close()

#close connection
con.close()








