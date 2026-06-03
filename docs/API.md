# PulseWell API Documentation

Base URL: `http://localhost:5000/api`

## Authentication

### POST `/auth/register`
Creates an employee or admin account.

```json
{
  "name": "Maya Srinivasan",
  "email": "maya@pulsewell.ai",
  "password": "password123",
  "department": "Engineering",
  "role": "employee"
}
```

### POST `/auth/login`
Returns a JWT token.

```json
{
  "email": "maya@pulsewell.ai",
  "password": "password123"
}
```

## Employees

### GET `/employees/me`
Protected. Returns current user profile.

### GET `/employees`
Admin only. Returns all employees.

## Stress Logs

### POST `/stress-logs`
Protected. Creates a daily check-in and calls the AI prediction service.

```json
{
  "stress_level": 7,
  "mood": "anxious",
  "sleep_hours": 5.5,
  "work_hours": 10,
  "deadline_pressure": 8,
  "notes": "Release deadline feels tight."
}
```

### GET `/stress-logs/me`
Protected. Returns current employee stress logs.

## Analytics

### GET `/analytics/organization`
Admin only. Returns organization-level stress, department comparison, and latest analytics.

## AI

### POST `/ai/predict`
Protected proxy to Flask `/predict`.

### POST `/ai/sentiment`
Protected proxy to Flask `/sentiment`.

```json
{ "text": "I feel exhausted by meetings." }
```

### POST `/ai/chat`
OpenAI API integration placeholder for the wellness assistant.

## Notifications

### GET `/notifications`
Protected. Returns burnout alerts, reminders, and report notifications.
