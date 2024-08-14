from twttr import shorten


def main():
    test_upper()
    test_lower()
    test_number()
    test_punctuation()

def test_upper():
    assert shorten("twIttEr") == "twttr"
    assert shorten("THIS IS UPPERCASE") == "THS S PPRCS"

def test_lower():
    assert shorten("TWiTTeR") == "TWTTR"
    assert shorten("this is lower") == "ths s lwr"


def test_number():
    assert shorten("0123456789") == "0123456789"

def test_punctuation():
    assert shorten("am,irre,za") == "m,rr,z"

