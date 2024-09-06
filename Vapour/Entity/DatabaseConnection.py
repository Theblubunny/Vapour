# connect to the MySQL database

import mysql.connector

class DatabaseConnection:
    def __init__(self):
        # when the object is created make a connection to the database
        self.conn = mysql.connector.connect(user='root', password='2392', host='127.0.0.1', database='SDB')

    # when this method is called just return a reference to the connection already created
    def getConnection(self):
        return self.conn

    def close(self):
        # close the database connection
        self.conn.close()

        
