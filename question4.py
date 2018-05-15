##### Question 4 #####
"""
Find the least common ancestor between two nodes on a
binary search tree. The least common ancestor is the
farthest node from the root that is an ancestor of both
nodes. For example, the root is a common ancestor of
all nodes on the tree, but if both nodes are descendents
of the root's left child, then that left child might be
the lowest common ancestor. You can assume that both
nodes are in the tree, and the tree itself adheres to
all BST properties. The function definition should look
like question4(T, r, n1, n2), where T is the tree
represented as a matrix, where the index of the list is
equal to the integer stored in that node and a 1
represents a child node, r is a non-negative integer
representing the root, and n1 and n2 are non-negative
integers representing the two nodes in no particular
order. For example, one test case might be

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
and the answer would be 3.
"""
"""
Forked Node and BST classes from code built in lesson:
Technical Interview -> Trees -> BST Practice
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        """
        Insert nodes to build tree
        """
        if self.root:
            self.insert_helper(self.root, new_val)

    def insert_helper(self, start, new_val):
        if start:
            if new_val < start.value:
                if start.left:
                    self.insert_helper(start.left, new_val)
                else:
                    start.left = Node(new_val)
            else:
                if start.right:
                    self.insert_helper(start.right, new_val)
                else:
                    start.right = Node(new_val)

    def search(self, find_val):
        """
        Traverse BST until target node is found. Return list of
        ancestors for target node starting with root node and ending
        with parent.
        """
        return self.search_helper(self.root, find_val, parents=[])

    def search_helper(self, start, value, parents):
        if start:
            if value == start.value:
                return parents
            if value < start.value:
                parents.append(start.value)
                return self.search_helper(start.left, value, parents)
            if value > start.value:
                parents.append(start.value)
                return self.search_helper(start.right, value, parents)
        return parents


def question4(matrix, r, n1, n2):
    """
    Build binary search tree
    """
    bst = BST(r)
    for row in matrix:
        for index, item in enumerate(row):
            if item == 1:
                bst.insert(index)

    # Find all parents for target nodes n1 and n2 then iterate through
    # all common ancestors to find where list diverges. Least common
    # ancestor is last common item in list.
    n1_parents, n2_parents = bst.search(n1), bst.search(n2)
    lca = r
    for i in range(len(n1_parents)):
        if n1_parents[i] != n2_parents[i]:
            break
        lca = n1_parents[i]

    return lca


def main():
    m1 = [[0,0,0,0,0],
          [0,1,0,0,0],
          [0,0,0,0,1],
          [0,0,1,0,0],
          [1,0,0,0,0]]
    print("Question4: {0}".format(question4(m1, 3, 0, 2)))
    # result: 1

    m2 = [[0,0,0,0,0,0],
          [0,0,1,0,0,1],
          [1,0,0,0,0,0],
          [0,0,0,1,0,0],
          [0,1,0,0,0,0],
          [0,0,0,0,0,0]]
    print("Question4: {0}".format(question4(m2, 4, 0, 3)))
    # result: 2

    m3 = [[0,0,0,0,0,0],
          [1,0,0,0,0,0],
          [0,0,0,0,1,0],
          [0,1,0,0,0,0],
          [0,0,0,0,0,1],
          [0,0,0,1,0,0]]
    print("Question4: {0}".format(question4(m3, 2, 1, 5)))
    # result: 2

if __name__ == '__main__':
    main()
