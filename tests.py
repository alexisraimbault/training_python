import math

from my_lodash import trim, reverse, uniq, uniq_by, find, sort_by, group_by, flatten_deep, defaults_deep, xor

def floor_method(input):
    return math.floor(input)

def filter_by_age(user):
    return user['age'] < 18

def test_method(test_values):
    nb_valid = 0
    nb_total = len(test_values)
    for test_value in test_values:
        method = test_value['method']
        params = test_value['params']
        nb_params = len(params)
        expected_result = test_value['expected_result']

        if nb_params == 1:
            result = method(params[0])
        if nb_params == 2:
            result = method(params[0], params[1])
        
        is_valid = result == expected_result

        if is_valid:
            nb_valid += 1
        
    print('résultat : {0} / {1}'.format(nb_valid, nb_total))

test_object = [
    # trim
    {
        "method": trim,
        "params": ["   abc   "],
        "expected_result": "abc",
    },
    # reverse
    {
        "method": reverse,
        "params": [[1, 2, 3]],
        "expected_result": [3, 2, 1],
    },
    # uniq
    {
        "method": uniq,
        "params": [[2, 1, 2]],
        "expected_result": [2, 1],
    },
    # uniq_by
    {
        "method": uniq_by,
        "params": [[2.1, 1.2, 2.3], floor_method],
        "expected_result": [2.1, 1.2],
    },
    # find
    {
        "method": find,
        "params": [
            [
                { "name": "John", "age": 28 },
                { "name": "Jane", "age": 5 },
                { "name": "Jim",  "age": 54 },
                { "name": "Kate", "age": 40 }
            ], 
            filter_by_age
        ],
        "expected_result": { "name": "Jane", "age": 5 },
    },
    # sort_by
    {
        "method": sort_by,
        "params": [
            [
                { 'user': 'fred',   'age': 48 },
                { 'user': 'barney', 'age': 36 },
                { 'user': 'fred',   'age': 40 },
                { 'user': 'barney', 'age': 34 },
            ], 
            ['user', 'age']
        ],
        "expected_result": [
            { 'user': 'barney', 'age': 34 },
            { 'user': 'barney', 'age': 36 },
            { 'user': 'fred',   'age': 40 },
            { 'user': 'fred',   'age': 48 },
        ],
    },
    # group_by
    {
        "method": group_by,
        "params": [[6.1, 4.2, 6.3], floor_method],
        "expected_result": {
            4: [4.2],
            6: [6.1, 6.3],
        },
    },
    # flatten_deep
    {
        "method": flatten_deep,
        "params": [[1, [2, [3, [4]], 5]]],
        "expected_result": [1, 2, 3, 4, 5],
    },
    # defaults_deep
    {
        "method": defaults_deep,
        "params": [
            { 'a': { 'b': 2 } },
            { 'a': { 'b': 1, 'c': 3 } },
        ],
        "expected_result": { 'a': { 'b': 2, 'c': 3 } },
    },
    # xor
    {
        "method": xor,
        "params": [
            [2, 1],
            [2, 3],
        ],
        "expected_result": [1, 3],
    },
]

test_method(test_object)


