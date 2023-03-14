import sqlite3
import hashlib

class UserData:
    conn=sqlite3.connect("user_data.db")
    cur=conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS user_data(
        id INTEGER PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL)
        """
    )
    #TODO: create more user data
    #creating a hashed format of the password for its username
    username1="username1"
    hashed_password1 = hashlib.sha256("password123".encode()).hexdigest()
    cur.execute("INSERT INTO user_data (username,password) VALUES (?,?)",(username1,hashed_password1))

    conn.commit()

