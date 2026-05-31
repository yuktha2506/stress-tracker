# PulseWell: AI Employee Stress Tracker and Burnout Detection

PulseWell is a full-stack workplace wellness SaaS application for IT companies. It includes a polished React dashboard, JWT-secured Express APIs, MySQL persistence, and a Flask AI microservice for burnout prediction, sentiment analysis, and wellness recommendations.

## Project Structure

```text
stress_tracker/
  frontend/       React + Vite + Tailwind + Framer Motion UI
  backend/        Node.js + Express REST API with MVC structure
  ai-service/     Python Flask ML microservice
  database/       MySQL schema and seed data
  docs/           API and deployment documentation
```

## Frontend Setup

```bash
cd frontend
copy .env.example .env
npm install
npm run dev
```

Frontend runs at `http://localhost:5173`.

Demo login roles are selectable on the login screen:
- Employee: `maya@pulsewell.ai`
- HR/Admin: `hr@pulsewell.ai`

## Backend Setup

```bash
cd backend
copy .env.example .env
npm install
npm run dev
```

API runs at `http://localhost:5000`.

Important environment variables:
- `JWT_SECRET`
- `DB_HOST`
- `DB_USER`
- `DB_PASSWORD`
- `DB_NAME`
- `AI_SERVICE_URL`

## Database Setup

1. Start MySQL.
2. Run:

```bash
mysql -u root -p < database/schema.sql
mysql -u root -p < database/seed.sql
```

3. Update `backend/.env` with your MySQL credentials.

## AI Module Setup

```bash
cd ai-service
copy .env.example .env
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

AI service runs at `http://localhost:7000`.

Endpoints:
- `POST /predict`
- `POST /sentiment`
- `POST /recommendations`
- `POST /weekly-report`

## Features

- SaaS landing page with modern responsive UI
- Employee and HR/Admin role-based dashboards
- Daily stress, mood, sleep, workload, and deadline check-ins
- Burnout risk meter and AI wellness suggestions
- Organization analytics, high-risk employee table, trend charts, and heatmaps
- AI wellness chatbot with OpenAI API placeholder
- Notifications, break reminders, weekly reports, and settings
- JWT authentication, password hashing, validation, protected routes, and MySQL-safe parameterized queries

## Deployment

See `docs/DEPLOYMENT.md` for frontend, backend, AI service, and production hardening steps.
