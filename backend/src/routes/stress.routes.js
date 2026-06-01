import { Router } from 'express';
import { body } from 'express-validator';
import { create, mine } from '../controllers/stress.controller.js';
import { authenticate } from '../middleware/auth.middleware.js';
import { validate } from '../middleware/validate.middleware.js';

const router = Router();

router.get('/me', authenticate, mine);
router.post(
  '/',
  authenticate,
  [
    body('stress_level').isInt({ min: 1, max: 10 }),
    body('mood').trim().isLength({ min: 2 }),
    body('sleep_hours').isFloat({ min: 0, max: 24 }),
    body('work_hours').isFloat({ min: 0, max: 24 }),
    body('deadline_pressure').isInt({ min: 1, max: 10 }),
    body('notes').optional({ nullable: true }).isString().trim()
  ],
  validate,
  create
);

export default router;
