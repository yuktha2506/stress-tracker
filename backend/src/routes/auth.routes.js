import { Router } from 'express';
import { body } from 'express-validator';
import { login, register } from '../controllers/auth.controller.js';
import { validate } from '../middleware/validate.middleware.js';

const router = Router();

router.post(
  '/register',
  [
    body('name').trim().isLength({ min: 2 }),
    body('email').isEmail().normalizeEmail(),
    body('password').isLength({ min: 8 }),
    body('department').trim().isLength({ min: 2 }),
    body('role').isIn(['employee', 'admin'])
  ],
  validate,
  register
);

router.post('/login', [body('email').isEmail(), body('password').notEmpty()], validate, login);

export default router;
