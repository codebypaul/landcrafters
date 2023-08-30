import os
from dotenv import load_dotenv, find_dotenv
# import psycopg2
env_file=find_dotenv(".env")
load_dotenv(env_file)

# connection establishment
conn = psycopg2.connect(
database="postgres",
	user=os.environ.get("user"),
	password=os.environ.get("password"),
	host=os.environ.get("host"),
	port=os.environ.get("port")
)

conn.autocommit = True

# Creating a cursor object
cursor = conn.cursor()

# query to create a database
sql = ''' CREATE database products '''

# executing above query
cursor.execute(sql)
print("Database has been created successfully !!")

# Closing the connection
conn.close()
