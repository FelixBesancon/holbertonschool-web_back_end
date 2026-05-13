import readDatabase from '../utils';

export default class StudentsController {
  static getAllStudents(request, response) {
    let result = 'This is the list of our students\n';
    readDatabase(process.argv[2])
      .then((students) => {
        const fields = Object.keys(students)
          .sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
        for (const field of fields) {
          const fieldStudents = students[field];
          result += `Number of students in ${field}: ${fieldStudents.length}. List: ${fieldStudents.join(', ')}\n`;
        }
        response.send(result.trimEnd());
      })
      .catch((err) => {
        response.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(request, response) {
    const { major } = request.params;
    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }
    readDatabase(process.argv[2])
      .then((students) => {
        const fieldStudents = students[major];
        const result = `List: ${fieldStudents.join(', ')}\n`;
        response.send(result.trimEnd());
      })
      .catch((err) => {
        response.status(500).send('Cannot load the database');
      });
  }
}
