import pytest
from other_code.newTA import *

def test_05_createNewTA(ta_fixture) :
	#makes sure the data for the new TA works
	taInformation = taInfo()
	for i in range(len(ta_fixture)) :
		if taInformation[0] == ta_fixture[i] : 
			assert False
	assert isinstance(taInformation[1], int)

def test_05_createNewTAFail(ta_fixture) :
	#makes sure the data for the new TA works
	taInformation = taBadInfo()
	for i in range(len(ta_fixture)) :
		if taInformation[0] == ta_fixture[i] : 
			assert False
	assert isinstance(taInformation[1], int)

@pytest.fixture
def ta_fixture() :
	studentList = ["Greg" , "Ashley" , "Terry"]
	return studentList
