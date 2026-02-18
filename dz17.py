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


def evaluate_rpn(expression):
    stack = Stack()
    tokens = expression.split()
    for token in tokens:
        if token.isdigit() or token.startswith("-"):
            stack.push(int(token))
        elif token in "+-*/":
            if stack.size() < 2:
                raise ValueError("Недостаточно операндов")
            item_one = stack.pop()
            item_two = stack.pop()
            if token == "+":
                result = item_two + item_one
            if token == "-":
                result = item_two - item_one
            if token == "*":
                result = item_two * item_one
            if token == "/":
                result = item_two / item_one
            stack.push(result)
    return stack.pop()

print(evaluate_rpn("3 4 2 * +"))