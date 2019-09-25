import pytest
from other_code.loginAttempt import login

def test_tryLogin() :
	#tests if the login info is correct
	attempt = login()
	assert attempt[0] == "derek"
	assert attempt[1] == "password"
