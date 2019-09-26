import pytest
from other_code.newCourse import *

def test_createNewClass(class_fixture) :
	#makes sure the data for new course is acceptable
	newNumber = NEW_COURSE.get("classNum")
	assert isinstance(NEW_COURSE.get("courseName"), str)
	for i in range(len(class_fixture)) :
		if newNumber == class_fixture[i] :
			assert False

def test_createNewClassFail(class_fixture) :
	#makes sure the data for new course is acceptable
	newNumber = NEW_COURSE_FAIL.get("classNum")
	assert isinstance(NEW_COURSE_FAIL.get("courseName"), int)
	for i in range(len(class_fixture)) :
		if newNumber == class_fixture[i] :
			assert False

@pytest.fixture
def class_fixture() :
	currentClasses = ["CS3050" , "CS2380"]
	return currentClasses
