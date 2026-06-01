import app from './app.js';
import { env } from './config/env.js';

app.listen(env.port, () => {
  console.log(`Stress Tracker API running on port ${env.port}`);
});
