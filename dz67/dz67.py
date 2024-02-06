
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"Node {self.value}"


class Tree:
    tree_list = []



    def __init__(self,root:Node):
        self.root=root

    def in_order(self, node):
        if node is not None:
            self.in_order(node.left)
            print(node,end="-->")
            self.in_order(node.right)

    def post_order(self, node):
        if  node is not None :
            self.post_order(node.left)
            self.post_order(node.right)

            print(node, end="-->")

    def __contains__(self, data):
        return  self.find_parent_by_value(self.root, data)


    def find_parent_by_value(self, node, data):
        if node is not None:
            self.find_parent_by_value(node.left, data)
            self.find_parent_by_value(node.right, data)
            self.tree_list.append(node)
            for node in self.tree_list:
                if node.value ==data:
                    return node
            return False



if __name__=="__main__":

    tree=Tree(root=Node("A"))

    tree.root=Node("A")
    tree.root.left=Node("B")
    tree.root.left.left=Node("D")
    tree.root.left.right=Node("E")
    tree.root.left.left.left=Node("H")
    tree.root.left.left.right=Node("I")

    tree.root.right=Node("C")
    tree.root.right.left=Node("F")
    tree.root.right.right=Node("G")
    tree.root.right.right.left=Node("J")

    root=tree.root
    tree.in_order(root)
    print()
    tree.post_order(root)
    print()
    print("F" in tree)
    print(tree.find_parent_by_value(root,"F"))

