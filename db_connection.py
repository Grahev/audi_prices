import mariadb
import sys
import pyodbc

# Connect to MariaDB Platform
"""
try:
    conn = mariadb.connect(
        user="Krzysztof",
        password="7F#NB6GNCp9",
        host="192.168.1.101",
        port=3306,
        database="usedcarsni"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
"""
server_name = 'DESKTOP-5CNJJCA\SQLEXPRESS'

user_name = 'kgrac'

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-5CNJJCA\SQLEXPRESS;'
                      'Database=First_Database;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

# Get Cursor
cur = conn.cursor()


#conn.commit()
#print('added')



#create table
"""
cur.execute(
    CREATE IF NOT EXISTS TABLE test_crars (
        id int primary key auto_increment,
        employee_id int not null unique key,
        first_name varchar(30) not null,
        last_name varchar(30) not null)
)

"""


def insert_car_to_db(listing):
    title = listing['title']
    year = listing['year']
    price = listing['price'] 
    milage = listing['milage']
    transmission = listing['transmission']
    fuel_type = listing['fuel_type']
    body_style = listing['body_style']
    engine_size = listing['engine_size']
    doors = listing['doors']
    location = listing['location']
    id = listing['id']
    link = listing['link']
    timestamp = listing['timestamp']
    cur.execute(
        """INSERT INTO cars VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""",(title,year,price,milage,transmission,fuel_type,body_style,engine_size,doors,location,id,link,timestamp)
    )
    conn.commit()
    print(listing['title'])