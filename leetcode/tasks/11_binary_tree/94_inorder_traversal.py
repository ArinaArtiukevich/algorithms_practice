from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RecursiveSolution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def _inorder(current_root: TreeNode):
            if not current_root:
                return
            _inorder(current_root.left)
            res.append(current_root)
            _inorder(current_root.right)

        _inorder(root)
        return res


class IterativeSolution:
    def __init__(self, val: int = 0):
        self.root = TreeNode(val=val)

    def set_node(self, key: int, current_node: TreeNode) -> TreeNode:
        if current_node is None:
            current_node = self.root
        if current_node.left is None and current_node.right is None:
            if key > current_node.val:
                current_node.right = TreeNode(key)
                return current_node.right
            else:
                current_node.left = TreeNode(key)
                return current_node.left
        elif current_node.left is None:
            if key > current_node.val:
                self.set_node(key, current_node.right)
            else:
                current_node.left = TreeNode(key)
                return current_node.left
        elif current_node.right is None:
            if key < current_node.val:
                self.set_node(key, current_node.left)
            else:
                current_node.right = TreeNode(key)
                return current_node.right
        else:
            if key > current_node.val:
                self.set_node(key, current_node.right)
            else:
                self.set_node(key, current_node.left)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        cust_stack = []
        tmp = root
        while tmp or cust_stack:
            while tmp:
                cust_stack.append(tmp)
                tmp = tmp.left
            tmp = cust_stack.pop()
            res.append(tmp.val)
            tmp = tmp.right
        return res


if __name__ == '__main__':
    cbt = IterativeSolution(7)
    cbt.set_node(4, cbt.root)
    cbt.set_node(8, cbt.root)
    cbt.set_node(2, cbt.root)
    cbt.set_node(5, cbt.root)
    res = cbt.inorderTraversal(cbt.root)
    print(res)
