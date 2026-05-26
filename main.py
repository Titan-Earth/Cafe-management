"""
Cafe Management System - Main Application
"""
from database import Database
from models import Customer, MenuItem, Order, Staff
from utils import get_positive_int, get_positive_float, validate_phone
from datetime import datetime

class CafeManagementSystem:
    """Main application class"""
    
    def __init__(self):
        self.db = Database()
        self.customer = Customer(self.db)
        self.menu_item = MenuItem(self.db)
        self.order = Order(self.db)
        self.staff = Staff(self.db)
    
    def display_menu_items(self):
        """Display all menu items"""
        items = self.menu_item.get_all()
        if not items:
            print("✗ Menu is empty!")
            return
        
        print("\n" + "="*50)
        print("--- MENU ---")
        print("="*50)
        print(f"{'ID':<5} {'Item Name':<25} {'Price':<10}")
        print("-"*50)
        for item in items:
            print(f"{item['item_id']:<5} {item['item_name']:<25} Rs. {item['price']:<10}")
        print("="*50)
    
    def customer_section(self):
        """Customer interface"""
        print("\n" + "="*50)
        print("--- CUSTOMER REGISTRATION ---")
        print("="*50)
        
        name = input("Enter your name: ").strip()
        if not name:
            print("✗ Name cannot be empty!")
            return
        
        phone = input("Enter your phone number: ").strip()
        cust_id = self.customer.create(name, phone)
        
        if not cust_id:
            return
        
        while True:
            print("\n" + "="*50)
            print("--- CUSTOMER MENU ---")
            print("="*50)
            print("1. View Menu")
            print("2. Place Order")
            print("3. Cancel Order")
            print("4. View My Orders")
            print("5. Generate Bill")
            print("6. Logout")
            print("="*50)
            
            choice = input("Enter choice (1-6): ").strip()
            
            if choice == "1":
                self.display_menu_items()
            
            elif choice == "2":
                self.display_menu_items()
                item_name = input("\nEnter item name to order: ").strip()
                quantity = get_positive_int("Enter quantity: ")
                self.order.create(cust_id, item_name, quantity)
            
            elif choice == "3":
                orders = self.order.get_customer_orders(cust_id)
                if not orders:
                    print("✗ No orders to cancel!")
                    continue
                
                print("\nYour Orders:")
                for o in orders:
                    print(f"ID: {o['order_id']}, Item: {o['item_name']}, Qty: {o['quantity']}, Price: Rs. {o['price']}, Status: {o['status']}")
                
                order_id = get_positive_int("Enter Order ID to cancel: ")
                self.order.cancel(order_id, cust_id)
            
            elif choice == "4":
                orders = self.order.get_customer_orders(cust_id)
                if not orders:
                    print("✗ No orders yet!")
                else:
                    print("\n" + "="*50)
                    print("--- YOUR ORDERS ---")
                    print("="*50)
                    print(f"{'ID':<5} {'Item':<20} {'Qty':<5} {'Price':<10} {'Status':<10}")
                    print("-"*50)
                    for o in orders:
                        print(f"{o['order_id']:<5} {o['item_name']:<20} {o['quantity']:<5} Rs. {o['price']:<10} {o['status']:<10}")
                    print("="*50)
            
            elif choice == "5":
                orders = self.order.get_customer_orders(cust_id)
                if not orders:
                    print("✗ No orders yet!")
                else:
                    print("\n" + "="*50)
                    print("--- BILL ---")
                    print("="*50)
                    total = 0
                    for o in orders:
                        print(f"{o['item_name']} x{o['quantity']} = Rs. {o['price']}")
                        total += o['price']
                    print("-"*50)
                    print(f"Total Amount: Rs. {total}")
                    print("="*50)
                    print(f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
            elif choice == "6":
                print("\n✓ Thank you for your order! Goodbye!")
                break
            
            else:
                print("✗ Invalid choice!")
    
    def staff_section(self):
        """Staff interface"""
        print("\n" + "="*50)
        print("--- STAFF LOGIN ---")
        print("="*50)
        
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        
        staff_id = self.staff.authenticate(username, password)
        if not staff_id:
            print("✗ Invalid credentials!")
            return
        
        print("✓ Login Successful!")
        
        while True:
            print("\n" + "="*50)
            print("--- STAFF MENU ---")
            print("="*50)
            print("1. View All Orders")
            print("2. View All Customers")
            print("3. Add Menu Item")
            print("4. Remove Menu Item")
            print("5. Update Menu Item Price")
            print("6. Update Order Status")
            print("7. Logout")
            print("="*50)
            
            choice = input("Enter choice (1-7): ").strip()
            
            if choice == "1":
                orders = self.order.get_all()
                if not orders:
                    print("✗ No orders yet!")
                else:
                    print("\n" + "="*70)
                    print("--- ALL ORDERS ---")
                    print("="*70)
                    print(f"{'OrderID':<8} {'CustID':<8} {'Name':<15} {'Item':<20} {'Qty':<5} {'Price':<10} {'Status':<10}")
                    print("-"*70)
                    for o in orders:
                        print(f"{o['order_id']:<8} {o['cust_id']:<8} {o['name']:<15} {o['item_name']:<20} {o['quantity']:<5} Rs. {o['price']:<10} {o['status']:<10}")
                    print("="*70)
            
            elif choice == "2":
                customers = self.customer.get_all()
                if not customers:
                    print("✗ No customers yet!")
                else:
                    print("\n" + "="*50)
                    print("--- ALL CUSTOMERS ---")
                    print("="*50)
                    print(f"{'ID':<5} {'Name':<20} {'Phone':<15}")
                    print("-"*50)
                    for c in customers:
                        print(f"{c['cust_id']:<5} {c['name']:<20} {c['phone']:<15}")
                    print("="*50)
            
            elif choice == "3":
                item_name = input("Enter item name: ").strip()
                price = get_positive_float("Enter price: ")
                self.menu_item.create(item_name, price)
            
            elif choice == "4":
                self.display_menu_items()
                item_name = input("Enter item name to remove: ").strip()
                self.menu_item.delete(item_name)
            
            elif choice == "5":
                self.display_menu_items()
                item_id = get_positive_int("Enter item ID to update: ")
                price = get_positive_float("Enter new price: ")
                self.menu_item.update(item_id, price)
            
            elif choice == "6":
                orders = self.order.get_all()
                if not orders:
                    print("✗ No orders yet!")
                else:
                    order_id = get_positive_int("Enter Order ID: ")
                    print("Status options: pending, completed, cancelled")
                    status = input("Enter new status: ").strip().lower()
                    self.order.update_status(order_id, status)
            
            elif choice == "7":
                print("\n✓ Logged out successfully!")
                break
            
            else:
                print("✗ Invalid choice!")
    
    def run(self):
        """Main application loop"""
        try:
            while True:
                print("\n" + "="*50)
                print("===== WELCOME TO CAFE MANAGEMENT SYSTEM =====")
                print("="*50)
                print("1. Customer")
                print("2. Staff")
                print("3. Exit")
                print("="*50)
                
                choice = input("Enter choice (1-3): ").strip()
                
                if choice == "1":
                    self.customer_section()
                elif choice == "2":
                    self.staff_section()
                elif choice == "3":
                    print("\n✓ Thank you for using Cafe Management System!")
                    break
                else:
                    print("✗ Invalid choice!")
        
        except KeyboardInterrupt:
            print("\n\n✗ Application interrupted!")
        except Exception as e:
            print(f"\n✗ An error occurred: {e}")
        finally:
            self.db.close()


if __name__ == "__main__":
    app = CafeManagementSystem()
    app.run()
