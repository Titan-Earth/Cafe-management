# Cafe Management System

A professional Python-based Cafe Management System with improved security, OOP architecture, and comprehensive error handling.

## Features

### Customer Features
- Customer registration with phone validation
- Browse menu items
- Place orders with quantity validation
- Cancel orders
- View order history
- Generate itemized bills with timestamps

### Staff Features
- Secure login with hashed passwords
- View all orders with customer details
- View all customers
- Add/remove menu items
- Update menu item prices
- Update order status (pending, completed, cancelled)

## Security Improvements

✅ **Password Hashing**: SHA256 password hashing for staff accounts
✅ **Environment Variables**: Sensitive credentials stored in `.env` file
✅ **SQL Injection Prevention**: Parameterized queries throughout
✅ **Input Validation**: Phone, price, quantity validation
✅ **Error Handling**: Comprehensive try-except blocks
✅ **Database Constraints**: Foreign keys and unique constraints

## Architecture Improvements

- **OOP Design**: Separate classes for Customer, MenuItem, Order, and Staff
- **Modular Structure**: Separated concerns across multiple files
- **Database Abstraction**: Centralized database operations in `database.py`
- **Utility Functions**: Reusable validation and security functions
- **Configuration Management**: Environment-based configuration

## Project Structure

```
Cafe-management/
├── main.py                 # Main application entry point
├── database.py             # Database connection and operations
├── models.py               # Data models (Customer, Order, etc.)
├── utils.py                # Validation and security utilities
├── config.py               # Configuration and constants
├── database_schema.sql     # Database schema and sample data
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables
└── README.md               # Project documentation
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- MySQL Server
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/Titan-Earth/Cafe-management.git
cd Cafe-management
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Set Up Database

#### Option A: Using MySQL Command Line
```bash
mysql -u root -p < database_schema.sql
```

#### Option B: Using MySQL Workbench
1. Open MySQL Workbench
2. Open the `database_schema.sql` file
3. Execute the script

### Step 4: Configure Environment Variables

Edit `.env` file with your database credentials:
```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=cafe
```

### Step 5: Run the Application
```bash
python main.py
```

## Usage

### Customer Login
1. Select option "1. Customer" from main menu
2. Enter your name and phone number
3. Choose from available options:
   - View Menu
   - Place Order
   - Cancel Order
   - View My Orders
   - Generate Bill

### Staff Login
1. Select option "2. Staff" from main menu
2. Enter credentials:
   - **Username**: admin
   - **Password**: admin123
3. Access staff features

## Database Schema

### Tables

**customers**
- cust_id (Primary Key)
- name
- phone (Unique)
- created_at

**menu**
- item_id (Primary Key)
- item_name (Unique)
- price
- created_at

**orders**
- order_id (Primary Key)
- cust_id (Foreign Key)
- item_name (Foreign Key)
- quantity
- price
- status (pending, completed, cancelled)
- created_at

**staff**
- staff_id (Primary Key)
- username (Unique)
- password (SHA256 hashed)
- created_at

## Validation Rules

- **Phone**: Minimum 10 digits, numeric only
- **Quantity**: Positive integers only
- **Price**: Positive numbers (float)
- **Item Name**: Non-empty strings
- **Password**: SHA256 hashing

## Error Handling

- Database connection failures
- SQL execution errors
- Input validation errors
- Item not found scenarios
- Invalid login attempts
- Graceful application shutdown

## Future Enhancements

- [ ] User authentication with email verification
- [ ] Receipt printing functionality
- [ ] Sales analytics and reports
- [ ] Inventory management
- [ ] Discount and promo codes
- [ ] Payment integration
- [ ] Web interface using Flask/Django
- [ ] API development for mobile app
- [ ] User profile management
- [ ] Order tracking system

## Troubleshooting

### Database Connection Error
- Ensure MySQL server is running
- Check `.env` file credentials
- Verify database exists: `SHOW DATABASES;`

### Module Import Error
- Reinstall dependencies: `pip install -r requirements.txt`
- Ensure you're in the project directory

### Phone Validation Error
- Phone number must be at least 10 digits
- Only numeric characters allowed

## License

This project is open source and available under the MIT License.

## Author

Titan-Earth

## Support

For issues or questions, please open an issue on GitHub.
