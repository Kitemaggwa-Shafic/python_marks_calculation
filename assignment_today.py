# Assignment 
# 1. Using the assignment you have, modify it so that when someone enter a name which is not a string should get a message that the name should be a string
# 2. Marks should be between 20-100, beyond 100 and below 20 it should show an error
# 3. Before writing the txt file make sure that the user gets a message of the location of the file you have saved the file marks
# 4. Ensure that the course unit and course code are captured from the user
# 5. The user should that the passmark is 50% and should know whether she has passed or not ie below 50% failed and above 50% passed basing on the final mark

'''
# Assignment weekend Work

Brook University
software should help lecture in awarding course unit marks or grading , 
For each unit they have 2 tests ie tes1 and test2 and course works for tests they take the best done 
and add on the course work marks and the average of the two is out of 40% its the course work marks

They have final exam marked out of 60% its exam marks
final marks of course unit = (course  work marks + exam marks)

As Py engineer, 
use atleast 3 dynamic functions which accept input of the name of student, academic year, test1, test2, 
course work marks and exam marks and compute the final course unit mark and it should be stored in a
text file called 'final_exam.txt'

** input ==> {nameOfstudent, academicYear, test1, test2, courseWork, examMarks, courseUnitMarks}
** print ==> {courseWork, examMarks, courseUnitMarks}

'''
# Assignment Adjustments Needed
# 1. Using the assignment you have, modify it so that when someone enter a 
# 		name which is not a string should get a message that the name should be a string
# 2. Marks should be between 20-100, beyond 100 and below 20 it should show an error
# 3. Before writing the txt file make sure that the user gets a message of the location of the file you have saved the file marks
# 4. Ensure that the course unit and course code are captured from the user
# 5. The user should that the passmark is 50% and should know whether she has passed or not 
# 		ie below 50% failed and above 50% passed basing on the final mark



# Declarig my variables to use for student, academic year, testa, test2, coursework
# Type casting studentName and academic year to strings
# Type casting test1, test2, course work to recieve Integer input values

studentNames = str(input('Please Enter Student Names : ' )) 
# studentAcademicYear = str(input('Please Enter Student Acadmic Year : ' ))
# courseUnitName = str(input('Please Course Unit Name : ' ))
# courseUnitCode = str(input('Please Course Unit Code : ' ))
tests1 = int(input('Please Enter Test One Marks Results : ' ))
tests2 = int(input('Please Enter Test Two Marks Results : '))
courseWork = int(input('Please Enter Coursework Marks Results : '))

  
# Mark limit tests function with < 20% and  > 100%
def markLimits():
	if tests1  and tests2 < 20:
		print("Test marks cant be below 20%")
	elif tests1 and tests2 > 100:
		print("Test marks cant be above 100%")
markLimits()		

# defining a function to help me compair the test results since 
# Will check to see which test has higher marks and will return that basing on the if stmts below
def testsComparison(tests1, tests2):
	if tests1 >= tests2:
		return tests1
	else:
		return tests2 
# print(testsComparison(test1,test2))  # testing if this Will return a test with higher marks

# functions for finalAvgCourseWorks, finalCourseUnitMarks
def finalAvgCourseWorks(courseWork):
    daBestTestOfTests = testsComparison(tests1, tests2)
    avgCourseWorks = (daBestTestOfTests + courseWork) / 2
    finalCalcAverage = round(avgCourseWorks * 0.40 )
    return finalCalcAverage
finalAvgCourseWorks(courseWork) 
print("Your Average course work marks are :" ,finalAvgCourseWorks(courseWork) ,"%")
print("--------------------------------------------------------------")

def finalCourseUnitMarks():
	finalExamMark = round(((courseWork + finalAvgCourseWorks(courseWork) ) * 0.60))
	return finalExamMark
finalCourseUnitMarks()
print(studentNames,"your Final Course Unit Exam Marks are :" ,finalCourseUnitMarks() ,"%")
print("--------------------------------------------------------------")

# Function for Fail and Pass
def passOrFail():
	if finalCourseUnitMarks() > 50:
		print("Hello, ", studentNames, "YOU HAVE PASSED")
	else:
		print("Hello, ", studentNames, "YOU HAVE FAILED")

 


    
