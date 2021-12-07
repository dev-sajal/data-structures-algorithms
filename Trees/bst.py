import sys

from base_structs import BinaryNode
from tree_traversals import inorder, preorder

class BST:
    def insert(self, value, current_root: BinaryNode)-> BinaryNode:
        if not current_root:  # Root node doesn't exist or Empty Tree
            return BinaryNode(value)
        elif value < current_root.value:
            current_root.left_child = self.insert(value, current_root.left_child)
        else:
            current_root.right_child = self.insert(value, current_root.right_child)

        return current_root

    def search(self, key, current_root: BinaryNode)-> BinaryNode:
        if current_root.value == key:
            return current_root
        elif current_root.value < key:
            return self.search(key, current_root.right_child)
        else:
            return self.search(key, current_root.left_child)

    def min_value_node(self, current_root: BinaryNode)-> BinaryNode:
        if not current_root.left_child:
            return current_root
        else:
            return self.min_value_node(current_root.left_child)

    def max_value_node(self, current_root: BinaryNode)-> BinaryNode:
        if not current_root.right_child:
            return current_root
        else:
            return self.max_value_node(current_root.right_child)

    def delete(self, key, current_root: BinaryNode)-> BinaryNode:
        if not current_root:  # Root node doesn't exist or Empty Tree
            return current_root
        elif key > current_root.value:
            current_root.right_child = self.delete(key, current_root.right_child)
        elif key < current_root.value:
            current_root.left_child = self.delete(key, current_root.left_child)
        else:
            if current_root.left_child is None:
                return current_root.right_child
            elif current_root.right_child is None:
                return current_root.left_child

            inorder_successor = self.min_value_node(current_root.right_child)
            current_root.value = inorder_successor.value
            current_root.right_child = self.delete(inorder_successor.value, current_root.right_child)

        return current_root

    def sort(self, array)-> None:
        root = None
        for element in array:
            root = self.insert(element, root)

        # Inorder traversal of BST provides a sorted array
        # This function prints the element and not returns an array
        inorder(root)

    def print(self, current_root, indent, last):
        if current_root is not None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(f"Value={current_root.value}")
            self.print(current_root.left_child, indent, False)
            self.print(current_root.right_child, indent, True)


if __name__ == '__main__':
    root = None
    bst = BST()
    root = bst.insert(50, root)
    root = bst.insert(30, root)
    root = bst.insert(20, root)
    root = bst.insert(40, root)
    root = bst.insert(70, root)
    root = bst.insert(60, root)
    root = bst.insert(80, root)

    # Print Inorder traversal of the Tree
    inorder(root)

    print("\nDeleting 20")
    root = bst.delete(20, root)
    print("Inorder traversal of the modified tree")
    inorder(root)

    print("\nDeleting 30")
    root = bst.delete(30, root)
    print("Inorder traversal of the modified tree")
    inorder(root)

    print("\nDeleting 50")
    root = bst.delete(50, root)
    print("Inorder traversal of the modified tree")
    inorder(root)
    print()
