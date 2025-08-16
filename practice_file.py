import unittest
from unit_test_mult import *

class test_concepts(unittest.TestCase):
    def test_add(self):
        data=add(5,10)
        assert data==15

    def test_add_negative(self):
        data=add(5,10)
        assert data==12

    def test_subtract(self):
        data=subtract(10,5)
        assert data==5


    def test_subtract_negative(self):
        data=subtract(10,5)
        assert data==12


    def test_is_even(self):
        data=is_even(4)
        assert data==True

    def test_is_even_negative(self):
        data=is_even(5)
        assert data==True

    def test_is_odd(self):
        data=is_odd(7)
        assert data==True

    def test_is_odd_negative(self):
        data=is_odd(4)
        assert data==True

    def test_revstr(self):
        data=revstr("python")
        assert data == "nohtyp"

    def test_revstr_negative(self):
        data=revstr("python")
        assert data=="python"

    def test_get_max_value(self):
        data=get_max_value([1,2,3,4,5])
        assert data==5

    def test_get_max_value_negative(self):
        data=get_max_value([1,2,3,4,5])
        assert data==3

    def test_vowel_count(self):
        data=vowel_count("bangalore is great city")
        assert data==8


    def test_merge_dicts(self):
        data=merge_dicts({"a":1,"b":2},{"a":1,"b":4,"c":3})
        assert data=={"a":1,"b":4,"c":3}

    def test_merge_dicts_negative(self):
        data=merge_dicts({"a":1,"b":2},{"a":1,"b":4,"c":5})
        assert data=={"a":1,"b":4,"c":3}