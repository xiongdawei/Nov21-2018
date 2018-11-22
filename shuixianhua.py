class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

    def has_value(self,value):
        if self.data == value:
            return True
        else:
            return False
    def print_list(self,node):
        while node:
            print(node)
            node = node.next

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def add_item(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self,node):
        """
node must be node
        """
        count = 0
        current_node = node
        while current_node is not None:
            count+=1
            current_node = current_node.getNext()
        return count

    def List(self):
        temp = Node(None)
        return temp

    def index(self,item):
        count = 0
        previous = self.head
        Boolean = False
        while not Boolean:
            if previous!= item:
                previous = previous.getNext()
                count+=1
            else:
                Boolean = True
        return count

    def search(self,item):
        current_node = self.head
        result = []
        num = 1
        while current_node is not None:
            if current_node.has_value(item):
                result.append(num)
                num+=1
        if result is not None:
            return result, True
        else:
            return False
      
    
            
            
        
node1 = Node(1)       
    
"""
recursive data structure
"""
    
a = Node
temp = Node(93)
#print(temp.getData())
#print(temp.getNext())
print(node1.getData())
#print(node1.has_value(1))
#temp.print_list(node1)
b = Node(3)
node1.setNext(b)
node1.print_list(node1)

c = Linked_List()
print(c.size(node1))








