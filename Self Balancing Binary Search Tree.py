class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.size = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        return node.height if node else 0

    def size(self, node):
        return node.size if node else 0

    def balanceFactor(self, node):
        return self.height(node.left) - self.height(node.right)

    def rightRotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1

        y.size = self.size(y.left) + self.size(y.right) + 1
        x.size = self.size(x.left) + self.size(x.right) + 1

        return x

    def leftRotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1

        x.size = self.size(x.left) + self.size(x.right) + 1
        y.size = self.size(y.left) + self.size(y.right) + 1

        return y

    def insert(self, node, key):
        if not node:
            return Node(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        else:
            return node

        node.height = max(self.height(node.left), self.height(node.right)) + 1
        node.size = self.size(node.left) + self.size(node.right) + 1

        balance = self.balanceFactor(node)

        if balance > 1 and key < node.left.key:
            return self.rightRotate(node)

        if balance < -1 and key > node.right.key:
            return self.leftRotate(node)

        if balance > 1 and key > node.left.key:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        if balance < -1 and key < node.right.key:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

    def minNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def remove(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self.remove(node.left, key)
        elif key > node.key:
            node.right = self.remove(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self.minNode(node.right)
            node.key = temp.key
            node.right = self.remove(node.right, temp.key)

        node.height = max(self.height(node.left), self.height(node.right)) + 1
        node.size = self.size(node.left) + self.size(node.right) + 1

        balance = self.balanceFactor(node)

        if balance > 1 and self.balanceFactor(node.left) >= 0:
            return self.rightRotate(node)

        if balance > 1 and self.balanceFactor(node.left) < 0:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        if balance < -1 and self.balanceFactor(node.right) <= 0:
            return self.leftRotate(node)

        if balance < -1 and self.balanceFactor(node.right) > 0:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

    def find(self, node, key):
        if not node:
            return False
        if node.key == key:
            return True
        if key < node.key:
            return self.find(node.left, key)
        else:
            return self.find(node.right, key)

    def orderOfKey(self, node, key):
        if not node:
            return 0
        if key <= node.key:
            return self.orderOfKey(node.left, key)
        else:
            return self.size(node.left) + 1 + self.orderOfKey(node.right, key)

    def getByOrder(self, node, k):
        if not node:
            return -1
        leftSize = self.size(node.left)
        if k <= leftSize:
            return self.getByOrder(node.left, k)
        elif k == leftSize + 1:
            return node.key
        else:
            return self.getByOrder(node.right, k - leftSize - 1)

    def destroy(self, node):
        if node:
            self.destroy(node.left)
            self.destroy(node.right)
            del node

    def insertKey(self, key):
        self.root = self.insert(self.root, key)

    def removeKey(self, key):
        self.root = self.remove(self.root, key)

    def findKey(self, key):
        return self.find(self.root, key)

    def orderOf(self, key):
        return self.orderOfKey(self.root, key)

    def getBy(self, k):
        return self.getByOrder(self.root, k)
