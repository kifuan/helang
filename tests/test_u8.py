import pytest

from helang.u8 import U8
from helang.exceptions import CyberArithmeticException


a = U8([5, 3, 6])
b = U8([2, 6, 7])
c = U8([2])
a_b = [3, -3, -1]
b_a = [-3, 3, 1]
a_c = [3, 1, 4]
b_c = [0, 4, 5]

a_add_b = [7, 9, 13]
a_add_c = [7, 5, 8]

a_mul_b = [70]
a_mul_c = [10]


def test_u8_eq():
    assert a == a
    assert a == a.value
    assert a != b


def test_u8_subtraction():
    assert a-b == a_b
    assert b-a == b_a
    assert a-c == a_c
    assert b-c == b_c

    try:
        c - a
        pytest.fail('illegal operation: number - vector')
    except CyberArithmeticException:
        ...


def test_u8_addition():
    assert a+b == a_add_b
    assert a+c == a_add_c
    assert c+a == a+c


def test_u8_set_all():
    u8 = U8([1, 2, 3])
    u8[U8(0)] = U8(10)

    assert u8 == [10, 10, 10]


def test_u8_mul():
    assert a*b == a_mul_b
    assert a*c == a_mul_c
    assert a*c == c*a


def test_u8_compare():
    assert U8([1, 2, 3]) < U8([4, 5, 6])
    assert not U8([1, 5]) < U8([3, 4, 2])
    assert U8([1, 2]) <= U8([1, 2, 4])
    assert U8([4, 5, 6]) > U8([1, 3])
    assert U8([4, 5, 6]) >= U8([4, 2])
    assert U8([1, 2]) == U8([1, 2, 0])
    assert U8([2, 1]) != U8([1, 2])


def test_u8_empty_cache():
    assert object.__eq__(U8(), U8())
