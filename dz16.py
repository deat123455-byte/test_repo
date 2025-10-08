class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Стек пуст")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Стек пуст")

    def size(self):
        return len(self.items)

def is_valid_brackets(string):
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in string:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.size() == 0:
                return False
            if stack.peek() == pairs.get(char):
                stack.pop()
            else:
                return False
    return stack.size() == 0



