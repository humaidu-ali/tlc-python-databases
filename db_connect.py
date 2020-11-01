# Load the postgres module
import psycopg2

# Create a connection object
con = psycopg2.connect(database="my_db", user="postgres", password="postgres", host="127.0.0.1", port="5432")

# Create a cursor via the connection
cur = con.cursor()

#insert query
cur.execute("insert into users (id,firstname,lastname,email) values (4,'Barda','Maer','marda@g.com')")


# Query via the cursor
cur.execute("select * from users")

#fetching rows in db
rows = cur.fetchall()
for row in rows:
    print(row)

 #commiting insert query
con.commit()
#close cursor
cur.close()

#close connection
con.close()

