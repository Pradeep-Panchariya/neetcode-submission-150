class MinStack:

    def __init__(self):
        self.stack = []
        self.second_stack = []
        self.min = float('inf')
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min:
            self.min = val
            self.second_stack.append(self.min)
        elif self.second_stack:
            self.second_stack.append(self.second_stack[-1])
        else:
            self.second_stack.append(val)
            self.min = val
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.second_stack.pop()
            # if self.second_stack:
            #     self.min = self.second_stack[-1]
            
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        return self.second_stack[-1]

