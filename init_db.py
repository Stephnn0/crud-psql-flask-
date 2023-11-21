import psycopg2

conn = psycopg2.connect(database="postgres", host="localhost", user="stefanovitteri", password="", port="5432")
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS notesCrud (id serial PRIMARY KEY, name varchar(100), description varchar(100))''')

cur.execute('''INSERT INTO notesCrud (name, description) VALUES ('first note','desc')''')

conn.commit()

cur.close()
conn.close()