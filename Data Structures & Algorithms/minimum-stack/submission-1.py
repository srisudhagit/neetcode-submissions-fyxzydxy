class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        self.size = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.size == 0:
            minele = val
        else:
            minele = val if self.minstack and self.minstack[-1] > val else self.minstack[-1] 
        self.minstack.append(minele)
        self.size += 1

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        self.size -= 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
