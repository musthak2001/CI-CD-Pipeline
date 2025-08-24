# In-memory user database
users_db = {
    "alice": "password123",
    "bob": "mypassword"
}

def validate_user(username, password):
    """
    Check if username exists and password matches.
    """
    return users_db.get(username) == password
