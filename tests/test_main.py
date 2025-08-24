
from src.main import add
from src.main import login
def test_add_function():
    assert add(2,3) == 5
    assert add(0,3) == 3
    assert add(-2,-2) ==-4



def test_login_success():
    assert login("alice", "password123") == "Login successful"
    assert login("bob", "mypassword") == "Login successful"

def test_login_fail_wrong_password():
    assert login("alice", "wrongpass") == "Invalid username or password"

def test_login_fail_unknown_user():
    assert login("unknown", "any") == "Invalid username or password"
