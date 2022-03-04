noOfStudent = int(input("No. Of Student : "))

for i in range(noOfStudent):
    print(i)
    subjectArray = []
    markArray = []
    studentName = input("Enter Student Name : ")
    noOfSubject = int(input("Enter No. Of Subjects : "))
    totalMark = 0
    for j in range(noOfSubject):
        print(j)
        subjectName = input("Enter Subject Name : ")
        subjectArray.append(subjectName)
        mark = int(input("Enter Marks : "))
        markArray.append(mark)
        totalMark = totalMark+mark
        # print(subjectArray)
    average = totalMark/noOfSubject
    print(studentName, subjectArray, markArray, average)
    subjectArray.reverse()
    markArray.reverse()
    print(studentName, subjectArray, markArray)
    subjectArray.clear()
    markArray.clear()
    print(studentName, subjectArray, markArray)
