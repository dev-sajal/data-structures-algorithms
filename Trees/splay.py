from base_structs import BinaryNode


class Splay:

    def zig(self, current_root: BinaryNode)-> BinaryNode:
        """ Right Rotate """
        new_root: BinaryNode = current_root.left_child
        current_root.left_child = new_root.right_child
        new_root.right_child = current_root

        return new_root

    def zag(self, current_root: BinaryNode)-> BinaryNode:
        """ Left Rotate """
        new_root: BinaryNode = current_root.right_child
        current_root.right_child = new_root.left_child
        new_root.left_child = current_root

        return new_root

    def splay(self, key: int, current_root: BinaryNode)-> BinaryNode:
        if (current_root is None) or (current_root.value == key) or \
            (current_root.left_child) or (current_root.right_child):
            return current_root
        elif key < current_root.value:
            if key < current_root.left_child.value:  # Zig-Zig
                # Move the key node to Root->Left->Left
                current_root.left_child.left_child = self.splay(key, current_root.left_child.left_child)

                # Perform First rotation on Root
                current_root = self.zig(current_root)
            elif key > current_root.left_child.value:  # Zig-Zag
                # Move the key node to Root->Left->Right
                current_root.left_child.right_child = self.splay(key, current_root.left_child.right_child)

                if current_root.left_child.right_child:
                    current_root.left_child = self.zag(current_root.left_child)

            # Perform Second rotation on Root
            return current_root if current_root.left_child is None else self.zig(current_root)
        else:
            # Move the key node to Root->Right->Right
            if key > current_root.right_child.value:  # Zag-Zag
                current_root.right_child.right_child = self.splay(key, current_root.right_child.right_child)

                # Perform First rotation on Root
                current_root = self.zag(current_root)
            elif key < current_root.right_child.value:  # Zag-Zig
                # Move the key node to Root->Left->Right
                current_root.right_child.left_child = self.splay(key, current_root.right_child.left_child)

                if current_root.right_child.left_child:
                    current_root.right_child = self.zig(current_root.right_child)

            # Perform Second rotation on Root
            return current_root if current_root.right_child is None else self.zag(current_root)

    def search(self, key, current_root: BinaryNode)-> BinaryNode:
        return self.splay(key, current_root)

    def insert(self, key, current_root: BinaryNode)-> BinaryNode:
        if current_root is None:
            return BinaryNode(key)
        else:
            # This will bring key value to root, if exists
            # Or else Splay process will make last accessed
            # node as root
            current_root = self.search(key, current_root)
            if current_root.value == key:
                return current_root
            elif key < current_root.left_child.value:
                new_root = BinaryNode(key)
                new_root.right_child = current_root
                new_root.left_child = current_root.left_child
                current_root.left_child = None
            else:
                new_root = BinaryNode(key)
                new_root.left_child = current_root
                new_root.right_child = current_root.right_child
                current_root.right_child = None
            return new_root

    def delete(self, key, current_root: BinaryNode)-> BinaryNode:
        if current_root is None:
            return current_root
        else:
            current_root = self.search(key, current_root)
            if current_root.value != key:
                # Key not present in the tree
                return current_root
            elif current_root.left_child is None:
                current_root = current_root.right_child
                return current_root
            else:
                temp = current_root
                current_root = self.splay(key, current_root.left_child)
                current_root.right_child = temp.right_child
                del temp
            return current_root


if __name__ == '__main__':
