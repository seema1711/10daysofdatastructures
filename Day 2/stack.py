class Stack:
    def __init__(self,size=None,limit=1000):
        self.top_item = []
        self.size = 0
        self.limit = limit
    def peek(self):
        if not self.is_empty():
            return self.value[-1]
        else: 
            print("Stack is empty")
    def push(self,value):
        #print("Current stack:", self.top_item)
        #print("size",len(self.top_item))
        if self.has_space():
            item = self.top_item.append(value)
            self.size += 1
        else:
            print("No space!")
            
    def set_next_node(self):
        item = self.top_item.append(self.value)
        item = self.top_item
    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            top_item = self.top_item.pop()
            self.size -=1
            return top_item
        else: 
            print("Stack is empty")
    def has_space(self):
        if self.limit > self.size:
            return True
    def is_empty(self):
        return self.top_item == []

myStack = Stack()
print(myStack.push("Seema"))
print(myStack.push("Saharan"))
#print(myStack.pop())
print(myStack.peek())
print("empty",myStack.is_empty())


    
