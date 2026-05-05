import pytest
from testCalc import square
from testCalc import main

def main2():
    testPositive()
    testNegative()
    testZero()
    stringTesting()

def testPositive():
    assert square(3)==9
    assert square(4)==16

def testNegative():
    assert square(-2)==4
    assert square(-3)==9
def testZero():
    assert square(0)==0

def stringTesting():
    with pytest.raises(TypeError): #basically a tiny try/except, raise just highlights what you want with that error
        square("dog")
    
if __name__ == "__main__":
    main2()

#PyTEST
#F=Failed
#E=Hints for why
#To run do pytest useCalc.py
#AssertionError for Assert