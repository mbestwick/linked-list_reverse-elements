"""
You’re given the pointer to the head node of a linked list. Change the next
pointers of the nodes so that their order is reversed. The head pointer given
may be null meaning that the initial list is empty.

Input Format
You have to complete the Node* Reverse(Node* head) method which takes one
argument - the head of the linked list. You should NOT read any input from
stdin/console.

Output Format
Change the next pointers of the nodes that their order is reversed and return
the head of the reversed linked list. Do NOT print anything to stdout/console.

"""


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def Reverse(head):
    if not head:
        return head

    stack = []
    curr = head
    while curr:
        stack.append(curr.data)
        curr = curr.next

    new_head = Node(stack.pop())
    curr = new_head
    while stack:
        curr.next = Node(stack.pop())
        curr = curr.next
    return new_head
