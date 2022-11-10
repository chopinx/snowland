class TreeNode(object):
    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right


class AVLTree(object):
    def __init__(self, data: list):
        # TODO build the tree with given data
        self.root = None

    @staticmethod
    def add_before(node: TreeNode, new: TreeNode):
        # TODO
        pass
