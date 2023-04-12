def testCompare(tests1,tests2):
    tests1 = int(input('Please Enter Test One Marks Results : ' ))
    tests2 = int(input('Please Enter Test Two Marks Results : '))
    if tests1 >= tests2:
        return tests1
    else:
        return tests2

def courseWorkResult():
    bestDone = testCompare(tests1, tests2)
    avgTests = (bestDone + courseWorkMark )/2
    avgTestFinal = avgTests * 0.4
    courseWorkMark = int(input('Please Course Work Marks Results : ' ))
    return avgTestFinal

def examMarks():
    avgexamMark = (courseWorkResult() + testCompare(tests1,tests2)) /2
    examMark = avgexamMark * 0.6
    return examMark

#GEt
while True:
    try:
        studentName = str(input('Please Student Name : ' ))
        break
    except ValueError:
        print('Please characters : ' )
'''
studentNames = str(input('Please Enter Student Names : ' )) 
studentAcademicYear = str(input('Please Enter Student Acadmic Year : ' ))
courseUnitName = str(input('Please Course Unit Name : ' ))
courseUnitCode = str(input('Please Course Unit Code : ' ))
'''

# Tests, course work, exam marks
while True:
    try:
        # tests1, tests2 = testCompare(tests1, tests2) 
        courseWorkMark = print(courseWorkResult())
        # if statement comparing tests using the testCompare() function
        if testCompare() < 20 and testCompare() >100:
            raise ValueError
        break
    except ValueError:
        # Print result of the error msg
        print('Please test values are not below 20 and not above 100 : ' )
        




 