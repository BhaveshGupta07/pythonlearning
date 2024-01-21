class node:
    def __init__(self,value):
        self.data = value
        self.next= None
        
class linkedlist:
    def __init__(self):
        self.head = None
        self.count = 0
        
    def __len__(self):
        return self.count
    
    def insert_at_head(self,value):
        new_node = node(value)
        new_node.next=self.head
        self.head=new_node
        self.count=self.count+1
        
    def printhead(self):
        return self.head
    
    def __str__(self):
        current=self.head
        result=''
        while current!=None:
            result=result+str(current.data)+"-->"
            current=current.next
        return result[:-3]




l=linkedlist()
l.insert_at_head(1)
l.insert_at_head(2)
l.insert_at_head(3)
print(l)

index = int(input("Enter the index of the node to print: "))

# Get the value of the node at the given index
node_value = linkedlist.get_node(index)

if node_value is not None:
    print(f"The value of the node at index {index} is: {node_value}")
else:
    print("Invalid index!")