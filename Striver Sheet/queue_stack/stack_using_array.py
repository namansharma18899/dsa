class Stack:
    def __init__(self) -> None:
        self.arr : list= []

    def push(self, el):
        self.arr.append(el)

    def pop(self):
        return self.arr.pop() if len(self.arr)>=1 else -1

    def size(self):
        return len(self.arr)