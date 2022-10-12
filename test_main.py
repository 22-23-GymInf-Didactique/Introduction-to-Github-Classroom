from main import is_prime


def test_zero_or_one():
    assert not is_prime(0)
    assert not is_prime(1)


def test_two():
    assert is_prime(2)


def test_three():
    assert is_prime(3)


def test_four():
    assert not is_prime(4)
