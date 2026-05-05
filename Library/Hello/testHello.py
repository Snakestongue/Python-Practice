from hello import hello

def testHello():
    assert hello("David") == "Hello David"
    assert hello() == "Hello world"