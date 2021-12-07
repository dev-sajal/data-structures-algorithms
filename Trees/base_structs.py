class BinaryNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return f'''({self.left_child}<-|{self.value}|->{self.right_child})'''


class AVLNode(BinaryNode):
    def __init__(self, value) -> None:
        super().__init__(value)
        self.height = 1

    def __repr__(self):
        return f'''({self.left_child}<-|V={self.value},H={self.height}|->{self.right_child})'''
