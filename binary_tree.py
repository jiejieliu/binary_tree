

class Node(object):
    def __init__(self, element, lchild=None, rchild=None):
        self.element = element
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    def __init__(self, root=None):
        self.root = root

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur_node = queue.pop()
                if cur_node.lchild is None:
                    cur_node.lchild = node
                    return
                elif cur_node.rchild is None:
                    cur_node.rchild = node
                    return
                else:
                    queue.append(cur_node.lchild)
                    queue.append(cur_node.rchild)

    def width_circle(self):
        if self.root is None:
            return ''
        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur_node = queue.pop()
                print(cur_node.element, end='')
                if cur_node.lchild is not None:
                    queue.append(cur_node.lchild)
                if cur_node.rchild is not None:
                    queue.append(cur_node.rchild)

    def preorder(self, node):
        if node == None:
            return
        print(node.element, end='')
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self, node):
        if node == None:
            return
        self.inorder(node.lchild)
        print(node.element, end='')
        self.inorder(node.rchild)

    def postorder(self, node):
        if node == None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.element, end='')


if __name__ == '__main__':
    t = Tree()
    t.add(0)
    t.add(1)
    t.add(2)
    t.add(3)
    t.add(4)
    t.add(5)
    t.add(6)
    t.add(7)
    t.add(8)
    t.add(9)
    print("\n广度优先BFS")
    t.width_circle()
    print("\n前序遍历")
    t.preorder(t.root)
    print("\n中序遍历")
    t.inorder(t.root)
    print("\n后序遍历")
    t.postorder(t.root)
