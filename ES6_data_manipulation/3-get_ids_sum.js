export default function getStudentIdsSum(students) {
  // Use the reduce function to accumulate the sum of student IDs
  return students.reduce((total, student) => total + student.id, 0);
}
