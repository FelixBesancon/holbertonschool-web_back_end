import fs from 'fs';

export default function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.trim().split('\n');
      const keys = lines[0].split(',');
      const students = lines.slice(1)
        .filter((line) => line.trim() !== '')
        .map((line) => {
          const obj = {};
          line.split(',').forEach((value, index) => {
            obj[keys[index]] = value;
          });
          return obj;
        });

      const response = {};

      students.forEach((student) => {
        if (!response[student.field]) response[student.field] = [];
        response[student.field].push(student.firstname);
      });

      resolve(response);
    });
  });
}
