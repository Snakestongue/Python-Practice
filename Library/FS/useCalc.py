from testCalc import square
from testCalc import main
def main2():
    test()

def test():
    # try:
    #     assert square(2)== 4
    # except AssertionError:
    #     print("2 squared is not 4")
    # try:
    #     assert square(3) == 9
    # except AssertionError:
    #     print("3 squared is not 9")
    # try:
    #     assert square(-2) == 4
    # except AssertionError:
    #     print("-2 squared is not 4")
    # try:
    #     assert square(-3) == 9
    # except AssertionError:
    #     print("-3 squared is not 9")
    # try:
    #     assert square(0) == 0
    # except AssertionError:
    #     print("0 squared is not 0")
    
    assert square(0)==0
    assert square(2)==4
    assert square(-2) ==4
    assert square(-3)==9
    assert square(4)==16
    main()

if __name__ == "__main__":
    main2()