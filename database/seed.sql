USE stress_tracker;

INSERT INTO employees (name, email, password, department, role) VALUES
('Maya Srinivasan', 'maya@pulsewell.ai', '$2a$12$demoHashReplaceInProduction', 'Engineering', 'employee'),
('Jordan Lee', 'hr@pulsewell.ai', '$2a$12$demoHashReplaceInProduction', 'People Ops', 'admin'),
('Anika Rao', 'anika@pulsewell.ai', '$2a$12$demoHashReplaceInProduction', 'Engineering', 'employee'),
('Chris Morgan', 'chris@pulsewell.ai', '$2a$12$demoHashReplaceInProduction', 'Support', 'employee');

INSERT INTO stress_logs (employee_id, stress_level, mood, sleep_hours, work_hours, deadline_pressure, notes) VALUES
(1, 6, 'calm', 6.8, 8.5, 6, 'A little deadline pressure but manageable.'),
(3, 9, 'overwhelmed', 4.8, 11.5, 9, 'Too many incidents and release deadlines.'),
(4, 8, 'tired', 5.1, 10.0, 8, 'Support queue was intense today.');

INSERT INTO analytics (employee_id, burnout_score, risk_level) VALUES
(1, 58, 'MEDIUM'),
(3, 91, 'HIGH'),
(4, 88, 'HIGH');
