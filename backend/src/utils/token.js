import jwt from 'jsonwebtoken';
import { env } from '../config/env.js';

export function signToken(employee) {
  return jwt.sign({ id: employee.id, role: employee.role, email: employee.email }, env.jwtSecret, { expiresIn: env.jwtExpiresIn });
}
