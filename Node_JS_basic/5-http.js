const http = require('http');
const fs = require('node:fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('\nCannot load the database'));
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

      let response =`\nNumber of students: ${students.length}\n`;

      const fields = [...new Set(students.map((student) => student.field))];

      for (const field of fields) {
        const fieldStudents = students
          .filter((student) => student.field === field)
          .map((student) => student.firstname);
        response += `Number of students in ${field}: ${fieldStudents.length}. List: ${fieldStudents.join(', ')}\n`;
      }

      resolve(response.trimEnd());
    });
  });
}

const app = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
  }

  if (req.url === '/students') {
    countStudents(process.argv[2])
      .then((students) => {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end(`This is the list of our students${students}`);
  })
  .catch((err) => {
    res.writeHead(500, { 'Content-Type': 'text/plain' });
    res.end(`This is the list of our students${err.message}`);
    });
  }
});

app.listen(1245);

module.exports = app;
