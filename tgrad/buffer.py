import numpy as np
from llops import UnaryOps, BinaryOps, TernaryOps, ReduceOps
from typing import Tuple


# LazyBuffer is like a tensor without derivatives
class Buffer:  ## add laziness later
    def __init__(self, device: str, size: int, dtype: np.dtype): ## Create a dtype class later
        self = self
        self.device = device
        self.size = size
        self.dtype = dtype