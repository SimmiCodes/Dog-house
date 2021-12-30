import sqlite3


conn = None
cur = None
def convert_to_binary(filename):
    with open(filename,'rb') as file:
        data = file.read()
    return data

def connection():
    global conn, cur
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS add_dog(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, image BLOB, breed TEXT, gender TEXT, about TEXT, meet TEXT,price TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS customer(id INTEGER PRIMARY KEY AUTOINCREMENT,name1 TEXT,breed1 TEXT, number TEXT, feedback TEXT, dog_name TEXT, price1 TEXT)")


def insert_data(name, image, breed, gender, about, meet,price): 
    connection()
    img =  convert_to_binary(image)
    cur.execute("INSERT INTO add_dog(name, image, breed, gender, about, meet,price) VALUES(?,?,?,?,?,?,?)",(name, img, breed, gender, about, meet,price))
    close()

def select_all_data():
    connection()
    r = cur.execute("SELECT * FROM add_dog")
    records = r.fetchall()
    close()
    print(len(records))
    return records
    # return records

def select_breed():
    connection()
    r = cur.execute('Select DISTINCT breed from add_dog;')
    records = r.fetchall()
    close()
    print(records)
    return records

def select_by_breed(breed):
    connection()
    r = cur.execute('Select * from add_dog where breed =?',(breed,))
    records = r.fetchall()
    close()
    return records

def insert_customer_data(name1,breed1, number, feedback, dog_name,price1): 
    connection()
    cur.execute("INSERT INTO customer(name1,breed1, number, feedback, dog_name,price1) VALUES(?,?,?,?,?,?)",(name1,breed1, number, feedback, dog_name,price1))
    close()


def select_customer_detail():
    connection()
    r = cur.execute('Select * from customer')
    records = r.fetchall()
    close()
    return records

def remove_dog(id):
    connection()
    r = cur.execute('DELETE FROM add_dog where id=?',(id,))
    conn.commit()
    close()
        


def close():
    conn.commit()
    cur.close()
    conn.close()

# insert_data("name","image","breed","gender","about","meet")
# connection()
# close()
# select_all_data()
