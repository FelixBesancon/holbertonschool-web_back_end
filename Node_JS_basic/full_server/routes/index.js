import express from 'express';
import AppController from '../controllers/AppController';
import StudentsController from '../controllers/StudentsController';

export default express.Router()
  .get('/', AppController.getHomepage)
  .get('/students', StudentsController.getAllStudents)
  .get('/students/:major', StudentsController.getAllStudentsByMajor);
