const fs = require('node:fs');

function countStudents (path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.trim().split('\n');
      const keys = lines[0].split(',');
      const students = lines.slice(1)
        .filter(line => line.trim() !== '')
        .map(line => {
          const obj = {};
          line.split(',').forEach((value, index) => {
            obj[keys[index]] = value;
          });
          return obj;
        });

      console.log(`Number of students: ${students.length}`);

      const fields = [...new Set(students.map(student => student.field))];

      for (const field of fields) {
        const fieldStudents = students
          .filter(student => student.field === field)
          .map(student => student.firstname);
        console.log(`Number of students in ${field}: ${fieldStudents.length}. List: ${fieldStudents.join(', ')}`
        );
      }

      resolve();
    });
  });
}

module.exports = countStudents;
