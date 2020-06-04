class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    def is_circular_linked_list(self, input_list):
        one = input_list
        two = input_list
        while two != None:
            one = one.next
            if two.next != None:
                two = two.next.next
            else:
                return False
            if one is two:
                return True
        return False




