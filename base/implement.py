from base.interface import Seq
from base.structure import LinkedList, AVLTree


class Seq_DynamicArray(Seq):
    def __init__(self, A):
        self.array = [None]
        self.length = 0
        for x in A:
            self.insert_last(x)

    def __resize(self):
        if self.length + 1 > self.__capacity():
            new_array = [None] * (2 * self.__capacity())
        elif self.length * 3 < self.__capacity() and self.__capacity() > 1:
            new_array = [None] * (self.__capacity() // 2)
        else:
            return
        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array

    def __capacity(self):
        return len(self.array)

    def build(self, A):
        self.__init__(A)

    def get_at(self, i: int):
        if i >= self.length:
            raise Exception("range index out of bounds")
        return self.array[i]

    def set_at(self, i: int, x):
        if i >= self.length:
            raise Exception("range index out of bounds")
        self.array[i] = x

    def insert_first(self, x):
        self.__resize()
        for i in range(self.length):
            self.array[i + 1] = self.array[i]
        self.array[0] = x
        self.length += 1

    def delete_first(self):
        if self.length == 0:
            raise Exception("sequence is already empty")
        self.__resize()
        for i in range(self.length - 1):
            self.array[i] = self.array[i + 1]
        self.length -= 1

    def insert_last(self, x):
        self.__resize()
        self.array[self.length] = x
        self.length += 1

    def delete_last(self):
        if self.length == 0:
            raise Exception("sequence is already empty")
        self.__resize()
        self.length -= 1

    def insert_at(self, i: int, x):
        self.__resize()
        for j in range(i, self.length):
            self.array[j + 1] = self.array[j]
        self.array[i] = x
        self.length += 1

    def delete_at(self, i: int):
        if i >= self.length:
            raise Exception("range index out of bounds")
        self.__resize()
        for j in range(i + 1, self.length):
            self.array[j - 1] = self.array[j]
        self.length -= 1

    def len(self):
        return self.length


class Seq_LinkedList(Seq):

    def __init__(self, A):
        self.data = LinkedList(A)

    def build(self, A):
        self.__init__(A)

    def get_at(self, i: int):
        if i >= self.data.len or i < 0:
            raise Exception("range index out of bounds")
        node = self.data.head
        while i > 0:
            node = node.next
            i -= 1
        return node.val

    def set_at(self, i: int, x):
        if i >= self.data.len or i < 0:
            raise Exception("range index out of bounds")
        node = self.data.head
        while i > 0:
            node = node.next
            i -= 1
        node.val = x

    def insert_first(self, x):
        self.data.insert_first(x)

    def delete_first(self):
        return self.data.delete_first()

    def insert_last(self, x):
        self.data.insert_last(x)

    def delete_last(self):
        return self.data.delete_last()

    def insert_at(self, i: int, x):
        if i > self.data.len or i < 0:
            raise Exception("range index out of bounds")
        node = self.data.head
        while i > 0:
            node = node.next
            i -= 1
        if node == self.data.head:
            self.data.insert_first(x)
        elif node is None:
            self.data.insert_last(x)
        else:
            self.data.insert_after(node.prev, x)

    def delete_at(self, i: int):
        if i >= self.data.len or i < 0:
            raise Exception("range index out of bounds")
        node = self.data.head
        while i > 0:
            node = node.next
            i -= 1
        if node == self.data.head:
            self.data.delete_first()
        elif node == self.data.tail:
            self.data.delete_last()
        else:
            self.data.delete_after(node.prev)

    def len(self):
        return self.data.len


class Seq_AVLTree(Seq):

    def __init__(self, A):
        self.data = None
        l = list(A)
        if len(l) == 0:
            return
        if len(l) == 1:
            self.data = AVLTree(l[0])
            return
        mid = len(l) // 2
        lt = Seq_AVLTree(l[:mid])
        rt = Seq_AVLTree(l[mid + 1:])
        self.data = AVLTree(l[mid])
        self.data.set_left(lt.data)
        self.data.set_right(rt.data)
        self.data.keep_balance()

    def build(self, A):
        self.__init__(A)

    def _get_node_at(self, i: int):
        if i < 0 or i >= self.data.size:
            raise Exception("range index out of bounds")
        node = self.data
        while True:
            if i == 0:
                return node.subtree_first()
            elif node.left and i == node.left.size:
                return node
            elif node.left and i < node.left.size:
                node = node.left
            else:
                i -= (node.left.size if node.left else 0) + 1
                node = node.right

    def get_at(self, i: int):
        if i < 0 or i >= self.data.size:
            raise Exception("range index out of bounds")
        node = self._get_node_at(i)
        return node.val

    def set_at(self, i: int, x):
        if i < 0 or i >= self.data.size:
            raise Exception("range index out of bounds")
        node = self._get_node_at(i)
        node.val = x

    def insert_first(self, x):
        # print("------------------------------------------")
        if not self.data:
            self.data = AVLTree(x)
            return
        self.data.subtree_first().add_left_leaf(AVLTree(x))

    def delete_first(self):
        if not self.data:
            raise Exception("seq is already empty")
        if self.data.size == 1:
            self.data = None
            return
        return self.data.subtree_first().delete()

    def insert_last(self, x):
        if not self.data:
            self.data = AVLTree(x)
            return
        self.data.subtree_last().add_right_leaf(AVLTree(x))

    def delete_last(self):
        if not self.data:
            raise Exception("seq is already empty")
        if self.data.size == 1:
            self.data = None
            return
        return self.data.subtree_last().delete()

    def insert_at(self, i: int, x):
        if i < 0 or i >= self.data.size:
            raise Exception("range index out of bounds")
        old_node = self._get_node_at(i)
        old_val = old_node.val
        old_node.val = x
        if old_node.right:
            old_node.right.subtree_first().add_left_leaf(AVLTree(old_val))
        else:
            old_node.add_right_leaf(AVLTree(old_val))

    def len(self):
        if self.data:
            return self.data.size
        return 0

    def delete_at(self, i: int):
        if i < 0 or i >= self.data.size:
            raise Exception("range index out of bounds")
        if self.data.size == 1:
            self.data = None
            return
        old_node = self._get_node_at(i)
        old_node.delete()
