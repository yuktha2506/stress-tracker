CREATE DATABASE IF NOT EXISTS stress_tracker;
USE stress_tracker;

CREATE TABLE IF NOT EXISTS employees (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(120) NOT NULL,
  email VARCHAR(160) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  department VARCHAR(100) NOT NULL,
  role ENUM('employee', 'admin') NOT NULL DEFAULT 'employee',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS stress_logs (
  id INT AUTO_INCREMENT PRIMARY KEY,
  employee_id INT NOT NULL,
  stress_level TINYINT NOT NULL CHECK (stress_level BETWEEN 1 AND 10),
  mood VARCHAR(40) NOT NULL,
  sleep_hours DECIMAL(4,2) NOT NULL,
  work_hours DECIMAL(4,2) NOT NULL,
  deadline_pressure TINYINT NOT NULL CHECK (deadline_pressure BETWEEN 1 AND 10),
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_stress_employee FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE,
  INDEX idx_stress_employee_created (employee_id, created_at),
  INDEX idx_stress_created (created_at)
);

CREATE TABLE IF NOT EXISTS analytics (
  id INT AUTO_INCREMENT PRIMARY KEY,
  employee_id INT NOT NULL,
  burnout_score DECIMAL(5,2) NOT NULL,
  risk_level ENUM('LOW', 'MEDIUM', 'HIGH') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_analytics_employee FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE,
  INDEX idx_analytics_employee_created (employee_id, created_at),
  INDEX idx_analytics_risk (risk_level)
);

CREATE TABLE IF NOT EXISTS notifications (
  id INT AUTO_INCREMENT PRIMARY KEY,
  employee_id INT,
  title VARCHAR(160) NOT NULL,
  body TEXT NOT NULL,
  type ENUM('alert', 'wellness', 'report', 'system') NOT NULL DEFAULT 'system',
  is_read BOOLEAN NOT NULL DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_notifications_employee FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS anonymous_feedback (
  id INT AUTO_INCREMENT PRIMARY KEY,
  department VARCHAR(100),
  sentiment_label ENUM('POSITIVE', 'NEUTRAL', 'NEGATIVE') DEFAULT 'NEUTRAL',
  message TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
