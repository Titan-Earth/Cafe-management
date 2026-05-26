# Smart Secure Cafe Management System

A modern, intelligent Python-based Cafe Management System with enterprise-grade security, AI-powered insights, advanced OOP architecture, and comprehensive error handling.

## 🌟 Features

### Customer Features
- **Smart Customer Registration** with phone validation and profile management
- **Interactive Menu Browsing** with search and filtering capabilities
- **Intelligent Order Management** with quantity validation and recommendations
- **Smart Bill Generation** with itemized receipts and digital timestamps
- **Order Tracking** with real-time status updates
- **Purchase History** with analytics and insights

### Staff Features
- **Secure Multi-Role Login** with hashed passwords and session management
- **Comprehensive Order Management** with status tracking and filtering
- **Smart Customer Management** with history and preferences
- **Dynamic Menu Management** with price updates and availability control
- **Sales Analytics** with revenue reports and top-selling items
- **Inventory Insights** with stock level monitoring
- **User Activity Audit Logs** for transparency and accountability

### Smart Features
- **AI-Powered Recommendations** based on customer purchase history
- **Sales Analytics Dashboard** with revenue trends and insights
- **Peak Hours Detection** for optimal staffing
- **Inventory Optimization** alerts for low-stock items
- **Customer Loyalty Tracking** for repeat customers
- **Dynamic Pricing Suggestions** based on demand

## 🔒 Security Enhancements

✅ **Advanced Password Security**
- SHA256 password hashing with salt
- Password strength validation
- Secure password reset mechanism

✅ **Data Protection**
- Environment variables for sensitive credentials
- Parameterized SQL queries (SQL injection prevention)
- Data encryption for sensitive fields
- Secure session management

✅ **Input Validation & Sanitization**
- Phone number validation (10+ digits)
- Email validation and verification
- Price and quantity validation
- String sanitization against XSS
- Input length restrictions

✅ **Database Security**
- Foreign key constraints
- Unique constraints on critical fields
- Role-based access control (RBAC)
- Audit logging of all staff actions

✅ **Error Handling & Logging**
- Comprehensive exception handling
- Detailed error logging without exposing sensitive info
- Transaction rollback on failures
- Graceful error messages to users

## 🏗️ Architecture Improvements

- **Clean OOP Design**: Separate classes for Customer, MenuItem, Order, and Staff with clear responsibilities
- **Modular Structure**: Separated concerns across multiple files for maintainability
- **Database Abstraction Layer**: Centralized database operations for consistency
- **Utility Functions**: Reusable validation, security, and helper functions
- **Configuration Management**: Environment-based configuration with defaults
- **Design Patterns**: Factory, Singleton, and Strategy patterns implementation

## 📁 Project Structure

```
Cafe-management/
├── main.py                 # Main application entry point
├── database.py             # Database connection and operations
├── models.py               # Data models (Customer, Order, etc.)
├── utils.py                # Validation and security utilities
├── analytics.py            # Sales and business intelligence
├── config.py               # Configuration and constants
├── security.py             # Security utilities and encryption
├── database_schema.sql     # Database schema with indexes
├── requirements.txt        # Python dependencies
├── .env.example            # Example environment variables
├── .env                    # Environment variables (git ignored)
├── logs/                   # Application logs
│   └── audit.log          # Audit trail for staff actions
└── README.md              # Project documentation
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- MySQL Server 5.7+
- pip (Python package manager)
- Git

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

Copy `.env.example` to `.env` and update with your credentials:
```bash
cp .env.example .env
```

Edit `.env` with your database credentials:
```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_secure_password
DB_NAME=cafe_management
DB_PORT=3306
LOG_LEVEL=INFO
ENABLE_AUDIT_LOG=true
```

### Step 5: Run the Application
```bash
python main.py
```

## 💻 Usage

### Customer Login
1. Select **"1. Customer"** from main menu
2. Enter your name and phone number
3. Choose from available options:
   - View Menu (with search & filters)
   - Place Order (with AI recommendations)
   - Cancel Order
   - View My Orders & History
   - Generate Digital Bill
   - View Purchase Insights

### Staff Login
1. Select **"2. Staff"** from main menu
2. Enter credentials:
   - **Username**: `admin`
   - **Password**: `admin123` (change after first login)
3. Access staff features:
   - Dashboard with KPIs
   - Order Management
   - Customer Management
   - Menu Management
   - Sales Analytics
   - Audit Logs

## 📊 Database Schema

### Core Tables

**customers**
- `cust_id` (Primary Key)
- `name` (Indexed)
- `phone` (Unique, Indexed)
- `email` (Unique, Optional)
- `created_at`
- `updated_at`

**menu**
- `item_id` (Primary Key)
- `item_name` (Unique, Indexed)
- `description`
- `price`
- `stock_quantity`
- `category`
- `is_available`
- `created_at`

**orders**
- `order_id` (Primary Key, Indexed)
- `cust_id` (Foreign Key, Indexed)
- `item_name` (Foreign Key)
- `quantity`
- `price`
- `status` (pending, completed, cancelled)
- `created_at`
- `updated_at`

**staff**
- `staff_id` (Primary Key)
- `username` (Unique, Indexed)
- `password` (SHA256 hashed with salt)
- `role` (admin, manager, staff)
- `created_at`
- `last_login`

**audit_logs**
- `log_id` (Primary Key)
- `staff_id` (Foreign Key)
- `action`
- `details`
- `timestamp`

## ✅ Validation Rules

- **Phone**: Minimum 10 digits, numeric only
- **Email**: Valid email format (optional)
- **Quantity**: Positive integers only
- **Price**: Positive decimal numbers
- **Item Name**: Non-empty strings, max 100 characters
- **Password**: Min 8 chars, uppercase, lowercase, numbers, special chars
- **Username**: 4-20 alphanumeric characters + underscore

## 🛡️ Error Handling

- Database connection failures with retry logic
- SQL execution errors with transaction rollbacks
- Input validation errors with user-friendly messages
- Item not found scenarios with helpful suggestions
- Invalid authentication attempts with rate limiting
- Graceful application shutdown with cleanup

## 🔄 Logging & Monitoring

- **Application Logs**: DEBUG, INFO, WARNING, ERROR levels
- **Audit Logs**: All staff actions tracked with timestamps
- **Error Logs**: Detailed error information for debugging
- **Performance Logs**: Query execution times and bottlenecks

## 🚀 Future Enhancements

- [ ] Email verification and password reset
- [ ] Two-factor authentication (2FA)
- [ ] Receipt printing and PDF generation
- [ ] Advanced sales analytics and reporting
- [ ] Real-time inventory management
- [ ] Discount and promo code system
- [ ] Payment gateway integration (Stripe, PayPal)
- [ ] RESTful API development
- [ ] Web dashboard (Flask/Django)
- [ ] Mobile app API
- [ ] Machine learning for sales forecasting
- [ ] Customer feedback and ratings
- [ ] Notification system (Email/SMS)
- [ ] Multi-location support
- [ ] Docker containerization

## 🔧 Troubleshooting

### Database Connection Error
- Ensure MySQL server is running: `mysql -u root -p -e "SELECT 1"`
- Check `.env` file credentials match your MySQL setup
- Verify database exists: `SHOW DATABASES;`
- Check MySQL port (default: 3306)

### Module Import Error
- Reinstall dependencies: `pip install --upgrade -r requirements.txt`
- Ensure you're in the project directory
- Check Python version: `python --version` (3.8+ required)

### Authentication Issues
- Reset password in MySQL directly if needed
- Check audit logs in `logs/audit.log`
- Verify user role permissions

### Performance Issues
- Add database indexes on frequently queried columns
- Optimize queries in `database.py`
- Use connection pooling for multiple concurrent users
- Monitor query execution times in logs

## 📝 License

This project is open source and available under the **MIT License**.

## 👤 Author

**Titan-Earth**

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue on GitHub.

## 📞 Support

For issues, questions, or feature requests, please open an issue on [GitHub Issues](https://github.com/Titan-Earth/Cafe-management/issues).

---

**Made with ❤️ for the cafe industry**
