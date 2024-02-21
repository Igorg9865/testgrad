
class Tensor:
    pass

class Function:
    def __init__(self, device:str, *tensors:Tensor):
        self.device = device
        self.needs_input_grad = [t.requires_grad for t in tensors]
        self.requires_grad = True if any(self.needs_input_grad) else False #else None if None in self.needs_input_graph
    
