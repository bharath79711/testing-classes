
import unittest
from unit_test_mult import *
class TestMulti(unittest.TestCase):
    def test_multi(self):
        data=multi(2,3)
        assert data==6

    def test_multi2(self):
        data=multi(5,10)
        assert data==12
