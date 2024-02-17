import numpy as np
from llops import UnaryOps, BinaryOps, TernaryOps, ReduceOps, LoadOps, MovementOps
from typing import Union



# LazyBuffer is like a tensor without derivatives
class LazyBuffer:  ## add laziness later
    def __init__(self, buf: np.array): ## Create a dtype class later
        self = self
        self._np = buf
    def realized(self): return self._np
    
    def execute(self, op:Union[UnaryOps, BinaryOps, TernaryOps, ReduceOps, LoadOps, MovementOps]):
        return self 