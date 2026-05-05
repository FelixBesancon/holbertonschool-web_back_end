export default function getStudentIdsSum (listStudents) {
  return Array.isArray(listStudents) ? listStudents.reduce((acc, student) => acc + student.id, 0) : 0;
}
