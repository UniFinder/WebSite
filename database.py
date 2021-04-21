import mysql.connector

def log_in(email, password):
    db = mysql.connector.connect(
    host='192.168.0.23',
    user='pi',
    passwd='1234',
    database='Test',
    )
    mycursor = db.cursor()
    find_user = ("SELECT * FROM Members WHERE email = %s AND password = %s")
    mycursor.execute(find_user, [email, password])
    result = mycursor.fetchone()
    return result

def search_user(email):
    db = mysql.connector.connect(
    host='192.168.0.23',
    user='pi',
    passwd='1234',
    database='Test',
    )
    mycursor = db.cursor()
    find_user = ("SELECT * FROM Members WHERE email = %s")
    mycursor.execute(find_user, [email])
    result = mycursor.fetchone()
    return result


def sign_up(username, email, password):
    db = mysql.connector.connect(
    host='192.168.0.23',
    user='pi',
    passwd='1234',
    database='Test',
    )
    mycursor = db.cursor()
    result = search_user(email)
    if result == None:
        mycursor.execute("INSERT INTO Members (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
        db.commit()
        return True
    else:
        return False

def search_universities(country, major, price):
    db = mysql.connector.connect(
    host='192.168.0.23',
    user='pi',
    passwd='1234',
    database='Test',
    )
    mycursor = db.cursor()
    sql = ("SELECT * FROM Universities WHERE country = %s AND major = %s AND price = %s")
    mycursor.execute(sql, [country, major, price])
    result = mycursor.fetchall()
    return result