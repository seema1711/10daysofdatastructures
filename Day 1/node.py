#Creating a class
class Node:
    def __init__(self,value, link_node=None):
        self.value = value
        self.link_node = link_node
    def get_value(self):        #Function to get values
        return self.value
    def get_link_node(self):       #Function to get the value of link nodes 
        return self.link_node
    def set_link_node(self,link_node):        #Function to set the value of link nodes
        self.link_node = link_node

#Creating nodes
yacko = Node('likes to yak')
wacko = Node('has a penchant for hoarding snacks')
dot = Node('enjoys spending time in movie lots')

yacko.set_link_node(dot)
dot.set_link_node(wacko)

dots_data = yacko.get_link_node().get_value()
wackos_data = dot.get_link_node().get_value()
print(dots_data)
print(wackos_data)




