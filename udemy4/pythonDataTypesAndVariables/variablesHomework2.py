firstStudentName = input("Enter the student's name: ");
firstStudentId = int(input("Enter the student ID: "));
firstStudentGrade = float(input("Enter the student's grade: "));

secondStudentName = input("Enter the second student's name: ");
secondStudentId = int(input("Enter the second student ID: "));
secondStudentGrade = float(input("Enter the second student's grade: "));

print(
    "Information for students and their grades\n",
    firstStudentName, "(ID ", firstStudentId, ") got grade: ", firstStudentGrade ,"\n",
    secondStudentName, "(ID ", secondStudentId, ") got grade: ", secondStudentGrade,"\n",
    "average math grade: ", (firstStudentGrade+secondStudentGrade)/2
)


