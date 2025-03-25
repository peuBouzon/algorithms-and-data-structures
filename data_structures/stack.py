class Stack:
    def __init__(self):
        self._stack = []

    def push(self, x):
        self._stack.append(x)

    def pop(self):
        return self._stack.pop()

    def __iter__(self):
        return self

    def __next__(self):
        if not self._stack:
            raise StopIteration
        return self.pop()

if __name__ == '__main__':
    stack = Stack()
    for x in range(5):
        stack.push(x)
    for x in stack:
        print(x)