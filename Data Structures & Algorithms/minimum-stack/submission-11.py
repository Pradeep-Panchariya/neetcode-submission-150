class MinStack:

    def __init__(self):
        self.stack = []
        self.second_stack = []
        self.min = float('inf')
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.second_stack:
            self.second_stack.append(val)
        else:
            current_stack = self.second_stack[-1]
            self.second_stack.append(min(val,current_stack))
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.second_stack.pop()
            
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        return self.second_stack[-1]

