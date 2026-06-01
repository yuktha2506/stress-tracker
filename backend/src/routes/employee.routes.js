import { Router } from 'express';
import { authenticate, authorize } from '../middleware/auth.middleware.js';
import { index, me } from '../controllers/employee.controller.js';

const router = Router();

router.get('/me', authenticate, me);
router.get('/', authenticate, authorize('admin'), index);

export default router;
