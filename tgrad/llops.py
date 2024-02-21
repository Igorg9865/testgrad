import numpy as np
from enum import Enum, auto
from typing import Union, Dict, Callable  
import math

class UnaryOps(Enum): NOOP = auto(); EXP2 = auto(); LOG2 = auto(); SIN = auto(); SQRT = auto(); CAST = auto(); NEG = auto()
class BinaryOps(Enum): ADD = auto(); SUB = auto(); MUL = auto(); DIV = auto(); CMPEQ = auto(); CMPLT = auto(); MOD = auto(); MAX = auto(); XOR = auto()
class TernaryOps(Enum): WHERE = auto()                                                      # add MULACC later
class ReduceOps(Enum): SUM = auto(); MAX = auto()
class MovementOps(Enum): RESHAPE = auto(); PERMUTE = auto(); EXPAND = auto(); PAD = auto() # Add SHRINK + STRIDE later (maybe as_strided too)
class LoadOps(Enum): pass

Op = Union[UnaryOps, BinaryOps, ReduceOps]



