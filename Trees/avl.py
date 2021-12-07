from base_structs import AVLNode
from bst import BST
from tree_traversals import preorder


class AVL(BST):
    @staticmethod
    def get_height(node: AVLNode)-> int:
        # TODO: Implement a recursive method, without storing value for each node
        return node.height if node is not None else 0

    def updated_height(self, node: AVLNode)-> int:
        return 1 + max(self.get_height(node.left_child), self.get_height(node.right_child))

    def get_balance_factor(self, node: AVLNode)-> int:
        if node is None:   # Node doesn't exists
            return 0
        else:
            return self.get_height(node.left_child) - self.get_height(node.right_child)

    def left_rotate(self, unbalanced: AVLNode)-> AVLNode:
        new_root = unbalanced.right_child
        unbalanced.right_child = new_root.left_child
        new_root.left_child = unbalanced

        unbalanced.height = self.updated_height(unbalanced)
        new_root.height = self.updated_height(new_root)
        return new_root

    def right_rotate(self, unbalanced: AVLNode)-> AVLNode:
        new_root = unbalanced.left_child
        unbalanced.left_child = new_root.right_child
        new_root.right_child = unbalanced

        unbalanced.height = self.updated_height(unbalanced)
        new_root.height = self.updated_height(new_root)
        return new_root

    def insert(self, value, current_root: AVLNode)-> AVLNode:
        current_root = super().insert(value, current_root)
        current_root.height = self.updated_height(current_root)
        current_root = self.balance_tree(current_root)
        return current_root

    def balance_tree(self, node: AVLNode)-> AVLNode:
        balance_factor = self.get_balance_factor(node)
        if balance_factor < -1:
            if self.get_balance_factor(node.right_child) <= 0:
                # Right-Right Insertion Unbalanced
                return self.left_rotate(node)
            else:
                # Right-Left Insertion Unbalanced
                node.right_child = self.right_rotate(node.right_child)
                return self.left_rotate(node)
        elif balance_factor > 1:
            if self.get_balance_factor(node.left_child) >= 0:
                # Left-Left Insertion Unbalanced
                return self.right_rotate(node)
            else:
                # Left-Right Insertion Unbalanced
                node.left_child = self.left_rotate(node.left_child)
                return self.right_rotate(node)
        else:
            # Balance Factor is either {-1, 0, 1}, No balance needed
            return node

    def delete(self, key, current_root: AVLNode)-> AVLNode:
        current_root = super().delete(key, current_root)
        current_root.height = self.updated_height(current_root)
        current_root = self.balance_tree(current_root)
        return current_root


if __name__ == '__main__':
    tree = AVL()
    root = None

    for key in (9, 5, 10, 0, 6, 11, -1, 1, 2):
        root = tree.insert(key, root)

    print("Preorder traversal of the tree:")
    preorder(root)

    print("\nDeleting 10")
    root = tree.delete(10, root)
    print("After deletion preorder traversal:")
    preorder(root)

    print("\nDeleting -1")
    root = tree.delete(-1, root)
    print("After deletion preorder traversal:")
    preorder(root)
    print()
