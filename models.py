"""
Data models for Cafe Management System
"""
from database import Database
from utils import hash_password, verify_password, validate_phone, validate_price, validate_quantity
from datetime import datetime

class Customer:
    """Customer model"""
    
    def __init__(self, db):
        self.db = db
    
    def create(self, name, phone):
        """Add new customer"""
        if not validate_phone(phone):
            print("✗ Invalid phone number!")
            return None
        
        query = "INSERT INTO customers(name, phone, created_at) VALUES(%s, %s, NOW())"
        if self.db.execute_query(query, (name, phone)):
            result = self.db.fetch_one("SELECT LAST_INSERT_ID() as cust_id")
            if result:
                print(f"✓ Customer registered! ID: {result['cust_id']}")
                return result['cust_id']
        return None
    
    def get_all(self):
        """Get all customers"""
        return self.db.fetch_all("SELECT cust_id, name, phone, created_at FROM customers ORDER BY created_at DESC")
    
    def get_by_id(self, cust_id):
        """Get customer by ID"""
        query = "SELECT * FROM customers WHERE cust_id = %s"
        return self.db.fetch_one(query, (cust_id,))


class MenuItem:
    """Menu item model"""
    
    def __init__(self, db):
        self.db = db
    
    def get_all(self):
        """Get all menu items"""
        return self.db.fetch_all("SELECT item_id, item_name, price FROM menu ORDER BY item_name")
    
    def get_by_name(self, item_name):
        """Get menu item by name"""
        query = "SELECT item_id, item_name, price FROM menu WHERE item_name = %s"
        return self.db.fetch_one(query, (item_name,))
    
    def create(self, item_name, price):
        """Add new menu item"""
        if not validate_price(price):
            print("✗ Invalid price!")
            return False
        
        query = "INSERT INTO menu(item_name, price) VALUES(%s, %s)"
        if self.db.execute_query(query, (item_name, price)):
            print(f"✓ Item '{item_name}' added successfully!")
            return True
        return False
    
    def delete(self, item_name):
        """Remove menu item"""
        query = "DELETE FROM menu WHERE item_name = %s"
        if self.db.execute_query(query, (item_name,)):
            print(f"✓ Item '{item_name}' removed successfully!")
            return True
        return False
    
    def update(self, item_id, price):
        """Update menu item price"""
        if not validate_price(price):
            print("✗ Invalid price!")
            return False
        
        query = "UPDATE menu SET price = %s WHERE item_id = %s"
        if self.db.execute_query(query, (price, item_id)):
            print("✓ Item updated successfully!")
            return True
        return False


class Order:
    """Order model"""
    
    def __init__(self, db):
        self.db = db
    
    def create(self, cust_id, item_name, quantity):
        """Create new order"""
        if not validate_quantity(quantity):
            print("✗ Invalid quantity!")
            return False
        
        # Get item price
        menu_item = MenuItem(self.db).get_by_name(item_name)
        if not menu_item:
            print("✗ Item not found!")
            return False
        
        total_price = menu_item['price'] * quantity
        query = "INSERT INTO orders(cust_id, item_name, quantity, price, status, created_at) VALUES(%s, %s, %s, %s, 'pending', NOW())"
        
        if self.db.execute_query(query, (cust_id, item_name, quantity, total_price)):
            print(f"✓ Order placed successfully! Total: Rs. {total_price}")
            return True
        return False
    
    def get_customer_orders(self, cust_id):
        """Get all orders for a customer"""
        query = "SELECT order_id, item_name, quantity, price, status, created_at FROM orders WHERE cust_id = %s ORDER BY created_at DESC"
        return self.db.fetch_all(query, (cust_id,))
    
    def get_all(self):
        """Get all orders"""
        query = """SELECT o.order_id, o.cust_id, c.name, o.item_name, o.quantity, 
                   o.price, o.status, o.created_at FROM orders o 
                   JOIN customers c ON o.cust_id = c.cust_id ORDER BY o.created_at DESC"""
        return self.db.fetch_all(query)
    
    def cancel(self, order_id, cust_id):
        """Cancel order"""
        query = "DELETE FROM orders WHERE order_id = %s AND cust_id = %s"
        if self.db.execute_query(query, (order_id, cust_id)):
            print("✓ Order cancelled successfully!")
            return True
        print("✗ Order not found!")
        return False
    
    def update_status(self, order_id, status):
        """Update order status"""
        valid_statuses = ['pending', 'completed', 'cancelled']
        if status not in valid_statuses:
            print(f"✗ Invalid status! Must be one of: {', '.join(valid_statuses)}")
            return False
        
        query = "UPDATE orders SET status = %s WHERE order_id = %s"
        if self.db.execute_query(query, (status, order_id)):
            print(f"✓ Order status updated to '{status}'!")
            return True
        return False


class Staff:
    """Staff model"""
    
    def __init__(self, db):
        self.db = db
    
    def authenticate(self, username, password):
        """Authenticate staff member"""
        query = "SELECT staff_id, username, password FROM staff WHERE username = %s"
        result = self.db.fetch_one(query, (username,))
        
        if result and verify_password(password, result['password']):
            return result['staff_id']
        return None
    
    def create(self, username, password):
        """Create new staff account"""
        hashed_pwd = hash_password(password)
        query = "INSERT INTO staff(username, password) VALUES(%s, %s)"
        if self.db.execute_query(query, (username, hashed_pwd)):
            print(f"✓ Staff account '{username}' created!")
            return True
        return False
