import { Router } from 'express';
import { body } from 'express-validator';
import { chat, predict, sentiment } from '../controllers/ai.controller.js';
import { authenticate } from '../middleware/auth.middleware.js';
import { validate } from '../middleware/validate.middleware.js';

const router = Router();

router.post('/predict', authenticate, predict);
router.post('/sentiment', authenticate, [body('text').isString().trim().isLength({ min: 1 })], validate, sentiment);
router.post('/chat', authenticate, [body('message').isString().trim().isLength({ min: 1 })], validate, chat);

export default router;
