import pytest
from other_code.taSearch import taSearch

def test_tryTaSearch(student_fixture) :
	#makes sure the student being searched for is in the TA's class
	check = 0
	for i in range(len(student_fixture)) :
		if taSearch() == student_fixture[i]:
			check = 1
	if check == 0 :
		assert False

@pytest.fixture
def student_fixture() :
	studentList = ["Derek" , "K8lyn" , "Geoff"]
	return studentList
