from lowest_price import find_corresponding_prefixes, find_lowest_value

def test_find_corresponding_prefixes():
    assert find_corresponding_prefixes([('A', {1:0.9, 268:5.1, 46:0.17, 4620:0.0, 468:0.15, 4631:0.15, 4673:0.9, 46732:1.1}), ('B', {1:0.92, 44:0.5, 46:0.2, 467:1.0, 48:1.2})], 4673212345) == [(1.1, 'A', 46732), (1.0, 'B', 467)]

def test_find_lowest_value():
    assert find_lowest_value([(1.1, 'A', 46732), (1.0, 'B', 467)]) == {'operator_name':'B', 'prefix':467, 'value':1.0}