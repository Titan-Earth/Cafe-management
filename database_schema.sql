-- Create and use database
CREATE DATABASE IF NOT EXISTS cafe;
USE cafe;

-- Customers table
CREATE TABLE IF NOT EXISTS customers (
    cust_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    phone VARCHAR(15) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX(created_at)
);

-- Menu table
CREATE TABLE IF NOT EXISTS menu (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(50) NOT NULL UNIQUE,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX(item_name)
);

-- Orders table
CREATE TABLE IF NOT EXISTS orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    cust_id INT NOT NULL,
    item_name VARCHAR(50) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    status ENUM('pending', 'completed', 'cancelled') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cust_id) REFERENCES customers(cust_id) ON DELETE CASCADE,
    FOREIGN KEY (item_name) REFERENCES menu(item_name) ON DELETE RESTRICT,
    INDEX(cust_id),
    INDEX(status),
    INDEX(created_at)
);

-- Staff table with hashed passwords
CREATE TABLE IF NOT EXISTS staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX(username)
);

-- Insert sample staff account (password: admin123)
INSERT INTO staff(username, password) VALUES 
('admin', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3');

-- Insert sample menu items
INSERT INTO menu(item_name, price) VALUES 
('Coffee', 50),
('Tea', 30),
('Sandwich', 80),
('Burger', 120),
('Fries', 60),
('Cake', 100),
('Juice', 70),
('Cookies', 40);
