import calculator, pytest

def test_add():
    assert calculator.add(5, 3) == 8
    assert calculator.add(7,12) == 19

def test_subtract():
    assert calculator.subtract(5,3) == 2

def test_divide_by_zero():
    with pytest.raises(Exception): # pytest.raises is an assertion built into pytest. 
        # ^ This just says as long as there's an exception, it will pass!
        calculator.divide(10,0)

        