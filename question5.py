##### Question 5 #####
"""
Find the element in a singly linked list that's m elements
from the end. For example, if a linked list has 5 elements,
the 3rd element from the end is the 3rd element. The function
definition should look like question5(ll, m), where ll is
the first node of a linked list and m is the "mth number from
the end". You should copy/paste the Node class below to use
as a representation of a node in the linked list. Return the
value of the node at that position.

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def length(self):
        """
        Return length of linked list or return 0 if None.
        """
        length = 0
        current = self.head
        if self.head:
            length += 1
            while current.next:
                current = current.next
                length += 1
        return length

    def append(self, new_element):
        """
        Append nodes to linked list.
        """
        last = self.length()
        if last > 0:
            end = self.get_position(last)
            end.next = new_element

    def get_position(self, position):
        """
        Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list.
        """
        current = self.head
        currentPos = 1
        while currentPos < position:
            if current.next:
                current = current.next
                currentPos += 1
            else:
                return None
        return current


def question5(ll, m):
    """
    First, get length of linked list.
    Next, get data at requested position if position is 
    in list.
    """
    length = ll.length()
    node_val = None
    if length >= m and m > 0:
        node = ll.get_position(length - m + 1)
        node_val = node.data
    return node_val


def main():
    n1 = Node(101)
    n2 = Node(102)
    n3 = Node(103)
    n4 = Node(104)
    n5 = Node(105)
    n6 = Node(106)
    n7 = Node(107)
    n8 = Node(108)
    n9 = Node(109)

    ll = LinkedList(n1)
    ll.append(n2)
    ll.append(n3)
    ll.append(n4)
    ll.append(n5)
    ll.append(n6)
    ll.append(n7)
    ll.append(n8)
    ll.append(n9)

    print("Question5: {0}".format(question5(ll, 3)))
    # Result: 107

    print("Question5: {0}".format(question5(ll, 0)))
    # Result: None

    print("Question5: {0}".format(question5(ll, None)))
    # Result: None


if __name__ == '__main__':
    main()
