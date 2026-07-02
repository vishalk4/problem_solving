class MinStack:
    def __init__(self):
        self.stack = [] # main stack to store all elements
        self.min_stack = [] # Min stack to store minimum elements
    def push(self, val: int) -> None:
        self.stack.append(val) # push element to main stack
        # push to min_stack if:
        # min_stack is empty or current value is <= current minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    def pop(self) -> None:
        # check if the popped element is the current minimum
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop() # remove from main stack
    def top(self) -> int:
        return self.stack[-1] # return top element of stack
    def getMin(self) -> int:
        return self.min_stack[-1] # return current minimum element
