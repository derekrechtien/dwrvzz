import pytest
from other_code.loginAttempt import *

def test_tryLogin() :
	#tests if the login info is correct
	attempt = login()
	assert attempt[0] == "derek"
	assert attempt[1] == "password"

def test_tryLoginFail() :
	#test that should fail since has wrong login info passed in
	attempt2 = loginFail()
	assert attempt2[0] == "derek"
	assert attempt2[1] == "password"


