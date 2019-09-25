import pytest
from other_code.newCourse import NEW_COURSE

def test_createNewClass(class_fixture) :
	#makes sure the data for new course is acceptable
	newNumber = NEW_COURSE.get("classNum")
	for i in range(len(class_fixture)) :
		if newNumber == class_fixture[i] :
			assert False
	assert isinstance(NEW_COURSE.get("courseName"), str)

@pytest.fixture
def class_fixture() :
	currentClasses = ["CS3050" , "CS2380"]
	return currentClasses
