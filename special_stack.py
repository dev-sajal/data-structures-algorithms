EMPTY_MSG = "Empty Stack!"
FULL_MSG = "Stack Full!"

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"Node({self.value})"

    def __repr__(self) -> str:
        return f"Node({self.value})"


class Stack:
    def __init__(self, capacity=10):
        self.top = None
        self.count = 0
        self.capacity = capacity

    def __len__(self):
        return self.count

    def is_empty(self):
        return True if self.top is None else False

    def is_full(self):
        return True if self.count == self.capacity else False

    def push(self, value):
        if self.is_full():
            print(FULL_MSG)
        else:
            node = Node(value)
            if self.is_empty():
                self.top = node
            else:
                node.next = self.top
                self.top = node
            self.count += 1

    def pop(self):
        if self.is_empty():
            print(EMPTY_MSG)
        else:
            self.top, value = self.top.next, self.top.value
            return value


class MinStack(Stack):
    def __init__(self, capacity=10):
        super().__init__(capacity=capacity)
        self.minimum = None

    def push(self, value):
        if self.is_full():
            print(FULL_MSG)
        else:
            if self.is_empty():
                node = Node(value)
                self.top = node
                self.minimum = value
            elif value < self.minimum:
                temp = 2*value - self.minimum
                node = Node(temp)
                node.next = self.top
                self.top = node
                self.minimum = value
            else:
                node = Node(value)
                node.next = self.top
                self.top = node
            self.count += 1

    def pop(self):
        if self.is_empty():
            print(EMPTY_MSG)
        else:
            popped = self.top.value
            self.top = self.top.next
            if popped < self.minimum:
                self.minimum = 2*self.minimum - popped

            return popped

    def get_min(self):
        if self.top:
            return self.minimum
        else:
            print(EMPTY_MSG)


class MaxStack(Stack):
    def __init__(self, capacity=10):
        super().__init__(capacity=capacity)
        self.maximum = None

    def push(self, value):
        if self.is_full():
            print(FULL_MSG)
        else:
            if self.is_empty():
                node = Node(value)
                self.top = node
                self.maximum = value
            elif value > self.maximum:
                temp = 2*value - self.maximum
                node = Node(temp)
                node.next = self.top
                self.top = node
                self.maximum = value
            else:
                node = Node(value)
                node.next = self.top
                self.top = node
            self.count += 1

    def pop(self):
        if self.is_empty():
            print(EMPTY_MSG)
        else:
            popped = self.top.value
            self.top = self.top.next
            if popped > self.maximum:
                self.maximum = 2*self.maximum - popped

            return popped

    def get_max(self):
        if self.top:
            return self.maximum
        else:
            print(EMPTY_MSG)