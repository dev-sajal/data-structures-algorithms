from base_structs import BinaryNode

def inorder(root: BinaryNode):
    if root is not None:
        inorder(root.left_child)
        print(root.value, end=", ")
        inorder(root.right_child)


def preorder(root: BinaryNode):
    if root is not None:
        print(root.value, end=", ")
        preorder(root.left_child)
        preorder(root.right_child)


def postorder(root: BinaryNode):
    if root is not None:
        postorder(root.left_child)
        postorder(root.right_child)
        print(root.value, end=", ")


def levelorder(root: BinaryNode):
    queue = []
    queue.append(root)
    while queue:
        root = queue.pop()
        print(root.value, end=", ")

        if root.left_child:
            queue.append(root.left_child)

        if root.right_child:
            queue.append(root.right_child)
    print()
