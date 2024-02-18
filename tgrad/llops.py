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

def e(Op, i):
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


