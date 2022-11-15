import math
import time


class TreeNode(object):
    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right

        self.height = 0
        self.size = 1
        self.update_local_attrs()

    def subtree_first(self):
        """
        find the first node in traversal order of the subtree rooted by current node
        :return: None
        """
        if self.left is None:
            return self
        return self.left.subtree_first()

    def successor(self):
        """
        find successor in traversal order of current node in tree
        :return: None
        """
        if self.right is None:
            return self.parent
        return self.right.subtree_first()

    def subtree_insert_after(self, new):
        """
        insert a new node right after current node in traversal order of the subtree rooted by current node
        :param new: the new node
        :return: None
        """
        if self.right is None:
            self.set_right(new)
            return
        successor = self.successor()
        successor.set_left(new)

    def set_left(self, new):
        """
        set the left child of current node
        :param new: the new node
        :return: None
        """
        self.left = new
        if new:
            new.parent = self
        self.update_local_attrs()

    def update_local_attrs(self):
        """
        update local attributes of current node
        :return: None
        """
        self.height = 1 + max(self.left.height if self.left is not None else -1,
                              self.right.height if self.right is not None else -1)
        self.size = (self.left.size if self.left else 0) + (self.right.size if self.right else 0) + 1
        if self.parent:
            self.parent.update_local_attrs()

    def set_right(self, new):
        """
        set the right child of current node
        :return: None
        """
        self.right = new
        if new:
            new.parent = self
        self.update_local_attrs()


class AVLTree(TreeNode):

    def add_left_leaf(self, new):
        assert not (self.left and new.left and new.right)
        super().set_left(new)
        ancestor = self.parent
        while ancestor:
            ancestor.keep_balance()
            ancestor = ancestor.parent

    def keep_balance(self):
        if self.height_diff() < -1:
            self.left_rotate()
        elif self.height_diff() > 1:
            self.right_rotate()
        if self.parent:
            self.parent.keep_balance()

    def height_diff(self):
        return (self.left.height if self.left else -1) - (self.right.height if self.right else -1)

    def left_rotate(self):
        if not self.right:
            return
        if self.right.height_diff() > 0:
            # have to right rotate the right child first
            self.right.right_rotate()
        ns = [self.left, self, self.right, self.right.left, self.right.right]
        ns[1].val, ns[2].val = ns[2].val, ns[1].val
        ns[1].set_left(ns[2])
        ns[1].set_right(ns[4])
        ns[2].set_left(ns[0])
        ns[2].set_right(ns[3])

    def right_rotate(self):
        if not self.left:
            return
        if self.left.height_diff() > 0:
            # have to left rotate the left child first
            self.left.left_rotate()
        ns = [self.right, self, self.left, self.left.right, self.left.left]
        ns[1].val, ns[2].val = ns[2].val, ns[1].val
        ns[1].set_right(ns[2])
        ns[1].set_left(ns[4])
        ns[2].set_right(ns[0])
        ns[2].set_left(ns[3])

    def add_right_leaf(self, new):
        assert not (self.right and new.left and new.right)
        super().set_right(new)

    def display(self):
        q = [(self, 0, 0)]
        start = 0
        level_order = []
        curr_depth = 0
        row = ["  "] * (2 ** self.height)
        while len(q) > start:
            node, depth, order = q[start]
            if curr_depth != depth:
                print("[%d]" % curr_depth + "".join(row))
                row = ["  "] * (2 ** self.height * 2)
                curr_depth = depth
            if depth > self.height:
                break
            index = 2 ** (self.height - depth + 1) * order + 2 ** (self.height - depth) - 1
            row[index] = "{:0>2d}".format(node.val) if node else "__"
            if len(level_order) <= depth:
                level_order.append(0)
            start += 1
            if node:
                q.append((node.left, depth + 1, level_order[depth]))
                level_order[depth] += 1
                q.append((node.right, depth + 1, level_order[depth]))
            else:
                q.append((None, depth + 1, level_order[depth]))
                level_order[depth] += 1
                q.append((None, depth + 1, level_order[depth]))
            level_order[depth] += 1


if __name__ == '__main__':
    tree = AVLTree(0)
    for i in range(1, 100000):
        start = time.time()
        tree.subtree_first().add_left_leaf(AVLTree(i + 1))
        # print("------------------add %d, h=%d" % (i + 1, tree.height))
        # tree.display()
        # time.sleep(0.5)
        print(i, tree.height, tree.height // int(max(1, int(math.log2(i)))), int((time.time() - start)*10000))
