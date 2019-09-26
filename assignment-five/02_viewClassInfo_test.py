import pytest
from other_code.studentClasses import *

def test_viewClassInfo() :
	#tests if student is in the class they are looking at the info for
	check = 0
	ourList = classList()
	for i in range(len(ourList)) :
		if ourList[i] == "CS3050" :
			check = 1
	if check == 0 :
		assert False

def test_viewClassInfoFail() :
	#tests if student is in the class they are looking at the info for
	check = 0
	ourList = classListFail()
	for i in range(len(ourList)) :
		if ourList[i] == "CS3050" :
			check = 1
	if check == 0 :
		assert False
