export default function updateStudentGradeByCity (listStudents, city, newGrades) {
  return Array.isArray(listStudents)
    ? (
        listStudents
          .filter(student => student.location === city)
          .map(student => ({
            ...student,
            grade: newGrades.find(grade => grade.studentId === student.id)?.grade ?? 'N/A'
          }))
      )
    : [];
}
