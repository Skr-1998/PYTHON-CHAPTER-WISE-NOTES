class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty, cannot pop.")
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty, nothing to peek.")
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def display(self):
        print("Stack:", self.stack)

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

print("Peek:", stack.peek())

print("Popped:", stack.pop())

stack.display()
