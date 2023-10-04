export default function updateStudentGradeByCity(students, city, newGrades) {
  // Use filter to get the students from the specified city
  const filteredStudents = students.filter((student) => student.location === city);

  // Use map to update the grades based on newGrades
  const updatedStudents = filteredStudents.map((student) => {
    const matchingGrade = newGrades.find((grade) => grade.studentId === student.id);

    // If a matching grade is found, use it; otherwise, set the grade to 'N/A'
    const grade = matchingGrade ? matchingGrade.grade : 'N/A';

    // Create a new object with the updated grade
    return {
      ...student,
      grade,
    };
  });

  return updatedStudents;
}
