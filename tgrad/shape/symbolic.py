from typing import Optional

class Variable:
    def __init__(self, symbol:str, nmin:int, nmax:int):
        self.symbol = symbol
        self.min = nmin
        self.max = nmax
        self._val: Optional[int] = None
    def value(self):
        if (self._val is None): print("No Value available")
        else: return self._val
    def bind(self, val:int):
        if(val < self.min or self.max < val): return "Value is out of range"
        else: self._val = val
        return self
    def unbind(self):
        if(self._val is None): print("Cannot Unbind None")
        else: self._val = None