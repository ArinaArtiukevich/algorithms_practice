from io import klass
from queue import Queue
from typing import Optional, List


class CustomNode:
    def __init__(self, key, left_node: 'CustomNode' = None, right_node: 'CustomNode' = None, ):
        self.key = key
        self.left_node = left_node
        self.right_node = right_node


class CustomBinaryTree:
    def __init__(self, key: int = 0):
        self.root = CustomNode(key=key)

    def delete_node(self, key: int, parent_node: CustomNode = None) -> Optional[CustomNode]:
        if self.get_node(key, parent_node) is None:
            return None
        if key > parent_node.key:
            parent_node.right_node = self.delete_node(key, parent_node.right_node)
        elif key < parent_node.key:
            parent_node.left_node = self.delete_node(key, parent_node.left_node)
        else:
            if parent_node.right_node is None:
                return parent_node.left_node
            elif parent_node.left_node is None:
                return parent_node.right_node
            else:
                tmp_node = parent_node.right_node
                while tmp_node.left_node is not None:
                    tmp_node = tmp_node.left_node
                parent_node.key = tmp_node.key
                parent_node.right_node = self.delete_node(parent_node.key, parent_node.right_node)
        return parent_node

    def set_node(self, key: int, current_node: CustomNode) -> CustomNode:
        if current_node is None:
            current_node = self.root
        if current_node.left_node is None and current_node.right_node is None:
            if key > current_node.key:
                current_node.right_node = CustomNode(key)
                return current_node.right_node
            else:
                current_node.left_node = CustomNode(key)
                return current_node.left_node
        elif current_node.left_node is None:
            if key > current_node.key:
                self.set_node(key, current_node.right_node)
            else:
                current_node.left_node = CustomNode(key)
                return current_node.left_node
        elif current_node.right_node is None:
            if key < current_node.key:
                self.set_node(key, current_node.left_node)
            else:
                current_node.right_node = CustomNode(key)
                return current_node.right_node
        else:
            if key > current_node.key:
                self.set_node(key, current_node.right_node)
            else:
                self.set_node(key, current_node.left_node)

    def get_node(self, key: int, current_node: CustomNode) -> Optional[CustomNode]:
        if current_node is None:
            current_node = self.root
        if current_node.key == key:
            return current_node
        if current_node.left_node is None and current_node.right_node is None:
            return None
        elif current_node.left_node is None:
            if key > current_node.key:
                return self.get_node(key, current_node.right_node)
            else:
                return None
        elif current_node.right_node is None:
            if key < current_node.key:
                self.get_node(key, current_node.left_node)
            else:
                return None
        else:
            if key > current_node.key:
                return self.get_node(key, current_node.right_node)
            else:
                return self.get_node(key, current_node.left_node)

    def delete_node(self, key: int, parent_node: CustomNode = None) -> Optional[CustomNode]:
        if self.get_node(key, parent_node) is None:
            return None
        if key > parent_node.key:
            parent_node.right_node = self.delete_node(key, parent_node.right_node)
        elif key < parent_node.key:
            parent_node.left_node = self.delete_node(key, parent_node.left_node)
        else:
            if parent_node.right_node is None:
                return parent_node.left_node
            elif parent_node.left_node is None:
                return parent_node.right_node
            else:
                tmp_node = parent_node.right_node
                while tmp_node.left_node is not None:
                    tmp_node = tmp_node.left_node
                parent_node.key = tmp_node.key
                parent_node.right_node = self.delete_node(parent_node.key, parent_node.right_node)
        return parent_node

    # Increasing order!
    def inorder_traversal(self, current_node: CustomNode):
        if current_node.left_node:
            self.inorder_traversal(current_node.left_node)
        print(current_node.key)
        if current_node.right_node:
            self.inorder_traversal(current_node.right_node)

    def level_order_traversal(self, current_node: CustomNode):
        node_queue = Queue()
        node_queue.put(current_node)
        while not node_queue.empty():
            tmp = node_queue.get()
            if tmp:
                print(tmp.key)
                node_queue.put(tmp.right_node)
                node_queue.put(tmp.left_node)


if __name__ == '__main__':
    cbt = CustomBinaryTree(8)
    cbt.set_node(3, cbt.root)
    cbt.set_node(10, cbt.root)
    cbt.set_node(1, cbt.root)
    cbt.set_node(6, cbt.root)
    cbt.set_node(9, cbt.root)
    cbt.set_node(14, cbt.root)
    cbt.set_node(4, cbt.root)
    cbt.set_node(7, cbt.root)
    cbt.set_node(13, cbt.root)
    res_del = cbt.delete_node(100, cbt.root)
    cbt.level_order_traversal(cbt.root)
    print('d')
