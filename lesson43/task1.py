class Node(): 
 
    def __init__(self, data): 
        self.data = data
        self.left = None
        self.right = None
         
def inorder(temp):
 
    if (not temp):
        return
 
    inorder(temp.left) 
    print(temp.data,end = " ")
    inorder(temp.right) 
 
 
def insert(temp,key):
 
    if not temp:
        root = Node(key)
        return
    
    q = [] 
    q.append(temp) 
 
    # Do level order traversal until we find 
    # an empty place. 
    while (len(q)): 
        temp = q[0] 
        q.pop(0) 
 
        if (not temp.left):
            temp.left = Node(key) 
            break
        else:
            q.append(temp.left) 
 
        if (not temp.right):
            temp.right = Node(key) 
            break
        else:
            q.append(temp.right)
    
def deletion(root, key): 
    if(root == None): 
        return None
    if(root.left == None and root.right == None): 
        if(root.data == key): 
            return None
        else: 
            return root 
  
    key_node = None
    temp = None
    last = None
    q = [] 
    q.append(root) 
    # Do level order traversal to find deepest 
    # node(temp), node to be deleted (key_node) 
    # and parent of deepest node(last) 
    while(len(q)): 
  
        temp = q.pop(0) 
  
        if(temp.data == key): 
            key_node = temp 
        if(temp.left): 
  
            last = temp  # storing the parent node 
            q.append(temp.left) 
  
        if(temp.right): 
  
            last = temp  # storing the parent node 
            q.append(temp.right) 
  
    if(key_node != None): 
  
        key_node.data = temp.data  # replacing key_node's data to deepest node's data 
        if(last.right == temp): 
            last.right = None
        else: 
            last.left = None
  
    return root 
     
# Driver code 
if __name__ == '__main__':
    root = Node(10) 
    root.left = Node(11) 
    root.left.left = Node(7) 
    root.right = Node(9) 
    root.right.left = Node(15) 
    root.right.right = Node(8) 
 
    print("Inorder traversal before insertion:", end = " ")
    inorder(root) 
 
    key = 12
    insert(root, key) 
 
    print() 
    print("Inorder traversal after insertion:", end = " ")
    inorder(root)

    key = 12
    root = deletion(root, key)

    print() 
    print("Inorder traversal after insertion:", end = " ")
    inorder(root)