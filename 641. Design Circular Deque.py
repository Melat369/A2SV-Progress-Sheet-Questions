class MyCircularDeque:

    def __init__(self, k: int):
        # create a fixed size array of length k
        self.arr = [None for _ in range(k)]
        self.size = 0
        self.start = 0
        self.end = -1

    def insertFront(self, value: int) -> bool:
        if self.size == len(self.arr):
            return False
        self.start = (self.start - 1) % len(self.arr)
        self.arr[self.start] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == len(self.arr):
            return False
        self.end = (self.end + 1) % len(self.arr)
        self.arr[self.end] = value
        self.size += 1
        return True
        
    def deleteFront(self) -> bool:
        if self.size == 0:
            return False
        self.start = (self.start + 1) % len(self.arr)
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False
        self.end = (self.end - 1) % len(self.arr)
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.size == 0:
            return -1
        return self.arr[self.start]
        

    def getRear(self) -> int:
        if self.size == 0:
            return -1
        return self.arr[self.end]

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == len(self.arr)
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()