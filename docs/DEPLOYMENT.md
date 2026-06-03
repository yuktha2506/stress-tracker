# Deployment Steps

## Frontend
1. Set `VITE_API_URL` and `VITE_AI_URL` in `frontend/.env`.
2. Run `npm run build` in `frontend`.
3. Deploy `frontend/dist` to Vercel, Netlify, Azure Static Web Apps, or Nginx.

## Backend
1. Provision MySQL and run `database/schema.sql`.
2. Set secure production values in `backend/.env`.
3. Run `npm install --omit=dev`.
4. Start with `npm start` behind a process manager such as PM2.
5. Put the Express API behind HTTPS using Nginx, Azure App Service, Render, Railway, or AWS ECS.

## AI Service
1. Create a Python virtual environment.
2. Install `ai-service/requirements.txt`.
3. Start with `python app.py` or Gunicorn on Linux.
4. Replace the synthetic model with a trained artifact once historical data is available.

## Production Notes
- Use a managed MySQL instance with backups enabled.
- Rotate `JWT_SECRET` and store secrets in a vault.
- Restrict CORS to your frontend domain.
- Add rate limiting and audit logging before handling real employee health data.
- Keep employee notes private and aggregate analytics where possible.
