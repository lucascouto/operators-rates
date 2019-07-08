from lowest_price import *

def test_find_corresponding_prefixes():
    assert find_corresponding_prefixes([('A', {1:0.9, 268:5.1, 4620:0.0, 46732:1.1}), ('B', {467:1.0, 48:1.2})], 4673212345) == [(1.1, 'A', 46732), (1.0, 'B', 467)]

def test_find_lowest_value():
    assert find_lowest_value([(1.1, 'A', 46732), (1.0, 'B', 467)]) == ('B', 467, 1.0)