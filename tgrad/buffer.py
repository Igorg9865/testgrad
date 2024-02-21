import numpy as np
from llops import UnaryOps, BinaryOps, TernaryOps, ReduceOps, LoadOps, MovementOps
from typing import Union



# LazyBuffer is like a tensor without derivatives
class LazyBuffer:  ## add laziness later
    def __init__(self, buf: np.ndarray): ## Create a dtype class later
        self._np = buf
    
    @property
    def dtype(self): return self._np.dtype

    @property
    def realized(self): return self._np

    @property
    def shape(self): return self._np.shape

