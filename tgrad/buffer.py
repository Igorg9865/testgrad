from __future__ import annotations
import numpy as np
import math
from llops import Op ,UnaryOps, BinaryOps, TernaryOps, ReduceOps, LoadOps, MovementOps
from typing import Union



# LazyBuffer is like a tensor without derivatives
class LazyBuffer:  ## add laziness later
    def __init__(self, buf: np.ndarray): ## Create a dtype class later
        self._np = buf
    
    @property
    def dtype(self): return self._np.dtype

    @property
    def realized(self): return self._np # this creates a copy instead of a view

    @property
    def shape(self): return self._np.shape


    def e(self, Op, *i:LazyBuffer):
        if Op == UnaryOps.EXP2: return math.exp(i[0] * math.log(2)) # is this correct?
        if Op == UnaryOps.SIN: return math.sin(i[0])
        if Op == UnaryOps.SQRT: return math.sqrt(i[0])
        # UnaryOps.CAST
        if Op == UnaryOps.NEG: return -i[0]
        if Op == BinaryOps.ADD: return i[0] + i[1]
        if Op == BinaryOps.SUB: return i[0] - i[1]
        if Op == BinaryOps.MUL: return i[0] * i[1]
        if Op == BinaryOps.MOD: return i[0] % i[1]
        if Op == BinaryOps.XOR: return i[0] ^ i[1]
        if Op == BinaryOps.CMPEQ: return i[0] >= i[1]
        if Op == BinaryOps.CMPLT: return i[0] < i[1]
        if Op == BinaryOps.DIV: return i[0] // i[1] # if dtypes.is_int else i[0] / i[1] if i[1] != 0 else math.nan

