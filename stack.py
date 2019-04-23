class StackOverflowError(RuntimeError):
    pass


class StackIsEmptyError(RuntimeError):
    pass


class Stack:
    limit = 0
    def __init__(self, size):
        self.storage = [0] * size
        
    def push(self, v):
        if len(self.storage)>Stack.limit:
            self.storage[Stack.limit] = v
            Stack.limit += 1
        else:
            raise StackOverflowError

    def pop(self):
        if Stack.limit>0:
            a = self.storage[Stack.limit-1]
            self.storage[Stack.limit-1] = 0
            Stack.limit -= 1
            return a
        else:
            raise StackIsEmptyError
    def __len__(self):
        return Stack.limit

