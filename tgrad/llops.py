import numpy as np
from enum import Enum, auto
from typing import Union, Dict, Callable  

class UnaryOps(Enum): NOOP = auto(); EXP2 = auto(); LOG2 = auto(); SIN = auto(); SQRT = auto(); CAST = auto(); NEG = auto()
class BinaryOps(Enum): ADD = auto(); SUB = auto(); MUL = auto(); DIV = auto(); CMPEQ = auto(); CMPLT = auto(); MOD = auto(); MAX = auto(); XOR = auto()
class TernaryOps(Enum): pass
class ReduceOps(Enum): SUM = auto(); MAX = auto()
class MovementOps(Enum): pass
class LoadOps(Enum): pass

Ops = Union[UnaryOps, BinaryOps, ReduceOps]

op_fxn: Dict[Ops, Callable] = {
    UnaryOps.EXP2: np.exp2, UnaryOps.LOG2: np.log2, UnaryOps.SIN: np.sin, UnaryOps.NEG: np.negative, ## Add UnaryOps.cast later
    BinaryOps.ADD: np.add, BinaryOps.SUB: np.subtract, BinaryOps.MUL: np.multiply, BinaryOps.DIV: np.divide, 
    BinaryOps.CMPEQ: np.equal, BinaryOps.CMPLT: np.less, BinaryOps.MOD: np.mod, BinaryOps.MAX: np.maximum, BinaryOps.XOR: np.bitwise_xor,
    ReduceOps.SUM: np.sum, ReduceOps.MAX: np.max,
} 