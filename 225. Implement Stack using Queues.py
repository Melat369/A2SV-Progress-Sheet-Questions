class MyStack:

    def __init__(self):
        self.stack=[]

    def push(self, x: int) -> None:
        self.stack.append(x)        

    def pop(self) -> int:
        element=self.stack.pop()
        return element
        
    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return not self.stack


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop(int) 
# param_3 = obj.top()
# param_4 = obj.empty()