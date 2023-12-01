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

def reverse_sequence(input_sequence):
    stack = Stack()
    for char in input_sequence:
        stack.push(char)

    reversed_sequence = ''
    while not stack.is_empty():
        reversed_sequence += stack.pop()

    return reversed_sequence

if __name__ == "__main__":
    input_sequence = input("Enter a sequence of characters: ")
    reversed_result = reverse_sequence(input_sequence)
    print("Reversed sequence:", reversed_result)
