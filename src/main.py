from .my_users import validate_user
def add(a,b):
    return a+b

def login(username: str, password: str):
    """
    Attempt to login. Return message.
    """
    if validate_user(username, password):
        return "Login successful"
    return "Invalid username or password"