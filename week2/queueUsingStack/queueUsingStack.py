class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        tempStack = []
    
        while len(self.stack) > 1:
            tempStack.append(self.stack.pop())
        res = self.stack.pop()

        while tempStack:
            self.stack.append(tempStack.pop())
        return res

    def peek(self) -> int:
        tempStack = []
    
        while len(self.stack) > 1:
            tempStack.append(self.stack.pop())
        res = self.stack[0]

        while tempStack:
            self.stack.append(tempStack.pop())
        return res

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())
print(obj.pop())
print(obj.empty())
