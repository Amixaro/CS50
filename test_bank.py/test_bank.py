from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello there") == 0
    assert value("Hello, how are you?") == 0


def test_h():
    assert value("hi") == 20
    assert value("Hi") == 20
    assert value("hey") == 20
    assert value("Howdy") == 20
    assert value("Hola") == 20
def test_greeting():
    assert value("good morning") == 100
    assert value("Good evening") == 100
    assert value("Goodbye") == 100
    assert value("welcome") == 100
    assert value("Thank you") == 100
