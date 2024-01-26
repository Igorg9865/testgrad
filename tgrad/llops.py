import numpy as np
from enum import Enum, auto

class UnaryOps(Enum): NOOP = auto(); EXP2 = auto(); LOG2 = auto(); SIN = auto(); SQRT = auto(); CAST = auto(); NEG = auto()
class BinaryOps(Enum): ADD = auto(); SUB = auto(); MUL = auto(); DIV = auto(); CMPEQ = auto(); CMPLT = auto(); MOD = auto(); MAX = auto(); XOR = auto()
class ReduceOps(Enum): SUM = auto(); MAX = auto()