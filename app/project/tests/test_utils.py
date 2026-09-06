from utils import calculate_discount, is_even, get_full_name

def test_calculate_discount1():
    price = 540
    discount = 25
    expected = 135
    actual = calculate_discount(price, discount)
    assert expected == actual

def test_calculate_discount2():
    price = 200
    discount = 13
    expected = 26
    actual = calculate_discount(price, discount)
    assert expected == actual

def test_calculate_discount3():
    price = 200
    discount = 80
    expected = 160
    actual = calculate_discount(price, discount)
    assert expected == actual

def test_calculate_discount4():
    price = 777
    discount = 13
    expected = 101
    actual = calculate_discount(price, discount)
    assert expected == actual

def test_calculate_discount5():
    price = 100
    discount = 0
    expected = 0
    actual = calculate_discount(price, discount)
    assert expected == actual


def test_is_even1():
    number = 2
    expected = True
    actual = is_even(number)
    assert expected is actual

def test_is_even2():
    number = 3
    expected = False
    actual = is_even(number)
    assert expected is actual

def test_is_even3():
    number = -8
    expected = True
    actual = is_even(number)
    assert expected is actual

def test_is_even4():
    number = -5
    expected = False
    actual = is_even(number)
    assert expected is actual

def test_is_even5():
    number = 0
    expected = True
    actual = is_even(number)
    assert expected is actual


def test_get_full_name1():
    first_name = "john"
    last_name = "doe"
    expected = "John Doe"
    actual = get_full_name(first_name, last_name)
    assert expected == actual

def test_get_full_name2():
    first_name = "abc"
    last_name = "def"
    expected = "Abc Def"
    actual = get_full_name(first_name, last_name)
    assert expected == actual

def test_get_full_name3():
    first_name = "looooooooooong"
    last_name = "name"
    expected = "Looooooooooong Name"
    actual = get_full_name(first_name, last_name)
    assert expected == actual

def test_get_full_name4():
    first_name = "a"
    last_name = "b"
    expected = "A B"
    actual = get_full_name(first_name, last_name)
    assert expected == actual

def test_get_full_name5():
    first_name = "          John          "
    last_name = "   doe            "
    expected = "John Doe"
    actual = get_full_name(first_name, last_name)
    assert expected == actual
