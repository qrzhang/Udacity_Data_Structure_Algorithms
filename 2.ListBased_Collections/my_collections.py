"""Collections do not have a order
Lists: no fixed length
Arrays: each array has associated index, deletion one element could cause an empty box,
    or insertion should move all following boxes first. Inserting into an array is O(n), since
    you may need to shift elements to make space for the one you're inserting, or even copy
    everything to a new array if you run out of space. Thus, inserting into a Python list is
    actually O(n), while operations that search for an element at a particular spot are O(1).
(Doubled) Linked lists: have order but not indexes. Insertion and deletion are just the changes of pointers."""

# Linked list in Python
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

def append(self, new_element):
    current = self.head
    if self.head:
        while current.next:
            current = current.next
        current.next = new_element
    else:
        self.head = new_element