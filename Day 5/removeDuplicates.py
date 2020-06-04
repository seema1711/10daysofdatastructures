class Node:
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next = None
class removeDuplicates:
    def __init__(self):
        self.head = None
        self.tail = None
    def remove_duplicates(self):
        if (self.head == None):
            return
        else:
            current = self.head
            while (current!= None):
                index = current.next
                while (index != None):
                    if (current.data == index.data):
                        temp = index
                        index.previous.next = index.next
                        if (index.next != None):
                            index.next.previous = index.previous
                        temp = None
                    index = index.next
                current = current.next

