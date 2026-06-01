import { Router } from 'express';
import { organizationOverview } from '../controllers/analytics.controller.js';
import { authenticate, authorize } from '../middleware/auth.middleware.js';

const router = Router();

router.get('/organization', authenticate, authorize('admin'), organizationOverview);

export default router;
