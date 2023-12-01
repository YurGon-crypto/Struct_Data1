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

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

def are_parentheses_balanced(input_sequence):
    stack = Stack()
    opening_brackets = "({["
    closing_brackets = ")}]"

    for char in input_sequence:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty() or closing_brackets.index(char) != opening_brackets.index(stack.pop()):
                return False

    return stack.is_empty()

if __name__ == "__main__":
    input_sequence = input("Enter a sequence of characters: ")
    if are_parentheses_balanced(input_sequence):
        print("The parentheses, braces, and curly brackets are balanced.")
    else:
        print("The parentheses, braces, and curly brackets are not balanced.")
