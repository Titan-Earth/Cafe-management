"""
Database connection and operations
"""
import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

class Database:
    """Handles all database operations"""
    
    def __init__(self):
        self.con = None
        self.cur = None
        self.connect()
    
    def connect(self):
        """Establish database connection"""
        try:
            self.con = mysql.connector.connect(**DB_CONFIG)
            self.cur = self.con.cursor(dictionary=True)
            print("✓ MySQL Connection Successful!")
        except Error as e:
            print(f"✗ Error connecting to MySQL: {e}")
            raise
    
    def execute_query(self, query, params=None):
        """Execute query and return results"""
        try:
            if params:
                self.cur.execute(query, params)
            else:
                self.cur.execute(query)
            self.con.commit()
            return True
        except Error as e:
            print(f"✗ Database Error: {e}")
            self.con.rollback()
            return False
    
    def fetch_all(self, query, params=None):
        """Fetch all results"""
        try:
            if params:
                self.cur.execute(query, params)
            else:
                self.cur.execute(query)
            return self.cur.fetchall()
        except Error as e:
            print(f"✗ Database Error: {e}")
            return None
    
    def fetch_one(self, query, params=None):
        """Fetch single result"""
        try:
            if params:
                self.cur.execute(query, params)
            else:
                self.cur.execute(query)
            return self.cur.fetchone()
        except Error as e:
            print(f"✗ Database Error: {e}")
            return None
    
    def close(self):
        """Close database connection"""
        if self.cur:
            self.cur.close()
        if self.con:
            self.con.close()
        print("✓ Database connection closed.")
