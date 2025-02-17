
import pytest

from week11.src import calculator


@pytest.mark.parametrize("values,expected_result", [
    ([2, 2], 4),
    ([3, 3], 27),
    ([5, 0], 1),
])
def test_power(values, expected_result):
    base, exponent = values
    result = calculator.power(base, exponent)
    assert result == expected_result


@pytest.mark.parametrize("value,expected_result", [
    (2, 2),
    (3, 6),
    (5, 120)
])
def test_factorial(value, expected_result):
    result = calculator.factorial(value)
    assert result == expected_result

@pytest.mark.parametrize("value,expected_result", [
    (2, True),
    (3, True),
    (4, False),
    (17, True),
])
def test_is_prime(value, expected_result):
    result = calculator.is_prime(value)
    assert result == expected_result
