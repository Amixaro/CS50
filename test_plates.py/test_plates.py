from plates import is_valid


def test_starts_wth_two_letter():
    assert is_valid("CODE") == True
    assert is_valid("CS50") == True
    assert is_valid("C500") == False
    assert is_valid("H") == False


def test_plate_length():
    assert is_valid("OUTATIME") == False
    assert is_valid("AREALLYLONGPLATE") == False
    assert is_valid("LENGTH") == True


def test_zero_starting_number():
    assert is_valid("CS05") == False
    assert is_valid("NOZERO") == True


def test_ends_with_number():
    assert is_valid("50CS") == False
    assert is_valid("NUM1") == True
    assert is_valid("num5f0") == False


def test_alpha():
    assert is_valid("CS.50") == False
    assert is_valid("CS$50") == False
    assert is_valid("CS 50") == False
