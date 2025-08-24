
from src.main import add
def test_add_function():
    assert add(2,3) == 5
    assert add(0,3) == 3
    assert add(-2,-2) ==-4