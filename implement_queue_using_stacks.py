class MyQueue:
    def __init__(self):
        self.in_stack = [] # stack used for enqueue operation
        self.out_stack = []        # stack used for dequeue / peek operation
    def push(self, x):
        # Simply push into in_stack
        self.in_stack.append(x)
    def pop(self):
        # if out_stack is empty, transfer all elements
        if not self.out_stack: # move elements from in_stack to out_stack
            # this reverses order (LIFO → FIFO)
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        # pop from out_stack (front of queue)
        return self.out_stack.pop()
    def peek(self):
        # if out_stack is empty, transfer elements
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]# top of out_stack is the front of queue
    def empty(self):
        return not self.in_stack and not self.out_stack # queue is empty only if both stacks are empty
