class Stack:

    def __init__(self):
        self.stack = []

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        return self.stack.pop()

    def __iter__(self):
        return iter(self.stack)

    def __repr__(self) -> str:
        if len(self.stack) == 0:
            return "<empty stack>"
        else:
            return " ".join([str(x) for x in self.stack])


def test_stack():
    stack = Stack()
    print(f"New stack: {stack}")
    
    stack.push(1)
    stack.push(2)
    print(f"Added two elements: {stack}")

    el = stack.pop()
    print(f"Removed [{el}] from stack: {stack}")