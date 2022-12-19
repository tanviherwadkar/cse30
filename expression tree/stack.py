# assignment: programming assignment 4 (Expression Tree)
# author: Tanvi Herwadkar
# date: November 20, 2022
# file: stack.py implements a stack that can be used to keep track of elements
# methods: push(): pushes to stack
#          pop(): pops from stack
#          isEmpty(): returns boolean if stack is empty
#          peek(): returns top element
#          size(): returns num elements in stack

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.items != []:
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)
        
if __name__ == '__main__':

    data_in = ['hello', 'how', 'are', 'you']
    s = Stack()
    for i in data_in:
        s.push(i)

    assert s.size() == len(data_in)
    assert s.peek() == data_in[-1]
    data_out = []
    while not s.isEmpty():
        data_out.append(s.pop())
    assert data_out == data_in[::-1]
    assert s.size() == 0
    assert s.peek() == None