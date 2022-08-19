from helang.u8 import U8
from helang.quick_runner import quick_run_string


env = dict()


def setup():
    env.clear()


def test_parse_def():
    quick_run_string('''
        u8 list1 = 1 | 2 | 3;
        u8 list2 = [3];
    ''', env)

    assert env['list1'] == [1, 2, 3]
    assert env['list2'] == [0, 0, 0]


def test_parse_u8_set():
    quick_run_string('''
        u8 a = 1 | 2 | 3;
        u8 b = 4 | 5 | 6;
        a[1 | 3] = 12;
        b[0] = 10;
    ''', env)

    assert env['a'] == [12, 2, 12]
    assert env['b'] == [10, 10, 10]


def test_parse_u8_get():
    env['a'] = U8([2, 3, 4])
    quick_run_string('''
        u8 b = a[1 | 3];
    ''', env)

    assert env['b'] == [2, 4]


def test_parse_decl():
    quick_run_string('u8 a;', env)
    assert env['a'] == []


def test_parse_var_assign():
    quick_run_string('''
        u8 a = 1 | 2;
        a = 3 | 4;
    ''', env)

    assert env['a'] == [3, 4]


def test_parse_increment():
    quick_run_string('''
        u8 a = 1 | 2 | 3;
        a++;
    ''', env)

    assert env['a'] == [2, 3, 4]


def test_semicolon():
    quick_run_string("""
        ;;;u8 a = 1;;;
    """, env)

    assert env['a'] == [1]


def test_sub():
    quick_run_string('''
        u8 a = 4 | 6 | 7;
        u8 b = 2 | 3 | 4;
        u8 c = 1;
        u8 a_b = a - b;
        u8 a_b_c = a - b - c;
    ''', env)

    assert env['a_b'] == [2, 3, 3]
    assert env['a_b_c'] == [1, 2, 2]


def test_add():
    quick_run_string('''
        u8 a = 1 | 2 | 3;
        u8 b = 2;
        u8 c = 2 | 3 | 4;
        u8 a_add_b = a + b;
        u8 sum = a + b + c;
        u8 two = 1 + 1;
    ''', env)

    assert env['a_add_b'] == [3, 4, 5]
    assert env['sum'] == [5, 7, 9]
    assert env['two'] == [2]


def test_mul():
    quick_run_string('''
        u8 a = 1 | 2;
        u8 b = 2 | 3;
        u8 c = a * b;
    ''', env)

    assert env['c'] == [8]


def test_mixed_expr():
    quick_run_string('''
        u8 a = 1 | 2;
        u8 b = 3 | 4;
        u8 c = 5 | 8;
        u8 result = a + b * c + b;
    ''', env)

    assert env['result'] == [51, 53]
