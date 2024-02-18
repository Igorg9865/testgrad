# from test.test_ubt_ops import TestUops, TestIntUOps
from llops import UnaryOps, BinaryOps, TernaryOps, e
import math
import unittest


class TestUops(unittest.TestCase):
    def _equal_(self, val1, val2):
        self.assertEqual(val1, val2)

    def _test_uop_(self, op, fxn,):
        for a in [-2.0, 0.0, 1.0]:
            assert e(op, a) == fxn(a)
            ##_equal_(fxn[a], op)

class TestFloatUOps (TestUops):
   # def test_uop_exp2()
   # def test_uop_log2()
    def test_uop_sin(self): self._test_uop_(UnaryOps.SIN, lambda x: math.sin(x))
    def test_uop_sqrt(val, op=UnaryOps.SQRT, fxn=lambda x: math.sqrt(x)): assert e(op, val) == fxn(val[0]) # if val[0] >= 0 else math.nan <-- this part doesnt work
    #test_uop_cast
    def testing_neg(self): self._test_uop_(UnaryOps.NEG, lambda x: -x) 
    

if __name__ == '__main__':
    unittest.main(verbosity=2)