"""
Run tests by running the following cmd in the root dir: py.test
"""

from Code.utils import *
from Code.main import the
from Code.sym import Sym

def test_eg_sym():

    test_data = ["a","a","a","a","b","b","c"]
    column_name = 'Test Column 1'
    column_position = 1001

    expected_mode = 'a'
    expected_entropy = 1.379
    expected_freq_count = {'a': 4, 'b': 2, 'c': 1}

    test_num_obj = Sym(column_position, column_name);
    for i in test_data:
        test_num_obj.add(i)

    assert test_num_obj._has == expected_freq_count
    assert expected_mode == test_num_obj.mid()
    assert expected_entropy == round(test_num_obj.div(), 3)

    assert column_name == test_num_obj.getColumnName()
    assert column_position == test_num_obj.getColumnPosition()

def test_eg_the():
    oo(the)
    return True