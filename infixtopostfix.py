class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0


def is_operand(ch):
    return ch.isalnum()  # Returns True for alphabets or numbers


def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    return 0


def infix_to_postfix(infix):
    stack = Stack()
    postfix = []
    stack.push('#')  # Special marker for stack bottom

    for ch in infix:
        if is_operand(ch):
            postfix.append(ch)
        elif ch == '(':
            stack.push(ch)
        elif ch == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            if not stack.is_empty() and stack.peek() == '(':
                stack.pop()  # Remove '('
        else:
            while not stack.is_empty() and precedence(ch) <= precedence(stack.peek()):
                postfix.append(stack.pop())
            stack.push(ch)

    while not stack.is_empty() and stack.peek() != '#':
        postfix.append(stack.pop())

    return ''.join(postfix)


if __name__ == "__main__":
    infix_expression = "((a+b)*(c-d))"
    if not infix_expression.count('(') == infix_expression.count(')'):
        print("The infix expression is not balanced.")
    else:
        postfix_expression = infix_to_postfix(infix_expression)
        print("Postfix:", postfix_expression)
