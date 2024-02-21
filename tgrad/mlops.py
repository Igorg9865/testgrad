from tensor import Function
from llops import UnaryOps, BinaryOps, TernaryOps, e
from typing import Union

class Relu(Function):
    def forward(self, x:Union[int, float], y:Union[int, float]):
        self.relu = x.e(BinaryOps.MAX, )