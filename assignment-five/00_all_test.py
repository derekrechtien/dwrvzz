import pytest
from other_code.loginAttempt import login
from other_code.taSearch import taSearch
from other_code.studentClasses import classList
from other_code.newCourse import NEW_COURSE
from other_code.newTA import taInfo

def test_01_tryLogin() :
	#tests if the login info is correct
	attempt = login()
	assert attempt[0] == "derek"
	assert attempt[1] == "password"
	
def test_02_tryTaSearch(student_fixture) :
	#makes sure the student being searched for is in the TA's class
	check = 0
	for i in range(len(student_fixture)) :
		if taSearch() == student_fixture[i]:
			check = 1
	if check == 0 :
		assert False

def test_03_viewClassInfo() :
	#tests if student is in the class they are looking at the info for
	check = 0
	ourList = classList()
	for i in range(len(ourList)) :
		if ourList[i] == "CS3050" :
			check = 1
	if check == 0 :
		assert False

def test_04_createNewClass(class_fixture) :
	#makes sure the data for new course is acceptable
	newNumber = NEW_COURSE.get("classNum")
	for i in range(len(class_fixture)) :
		if newNumber == class_fixture[i] :
			assert False
	assert isinstance(NEW_COURSE.get("courseName"), str)

def test_05_createNewTA(ta_fixture) :
	#makes sure the data for the new TA works
	taInformation = taInfo()
	for i in range(len(ta_fixture)) :
		if taInformation[0] == ta_fixture[i] : 
			assert False
	assert isinstance(taInformation[1], int)

@pytest.fixture
def student_fixture() :
	studentList = ["Derek" , "K8lyn" , "Geoff"]
	return studentList

@pytest.fixture
def class_fixture() :
	currentClasses = ["CS3050" , "CS2380"]
	return currentClasses

@pytest.fixture
def ta_fixture() :
	studentList = ["Greg" , "Ashley" , "Terry"]
	return studentList


