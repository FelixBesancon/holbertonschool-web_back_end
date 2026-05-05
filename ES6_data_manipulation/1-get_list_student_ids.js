export default function getListStudentIds (listStudents) {
  return Array.isArray(listStudents) ? listStudents.map(student => student.id) : [];
}
