

class node(object):
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.key)

class BST(object):

    """ Class and most methods are based on CLRS, chapter 12
    
    Binary search tree property:
        - Let x be a node in a binary search tree. If y is a node in the left
        sub-tree of x, the y.key <= x.key. If y is a node in the right sub-tree
        of x, then y.key >= x.key 

    Class has the following methods:
        Note: 't' is denotes an instance in the following definitions
        - get_root: returns the root of the BST 
        - get_node(k): k is a node key, returns k if node in tree
        - show_node(k): prints the key,l_child, and r_child for node k in tree
        - show_tree(): prints the whole tree, showing each parents node in relation to its children
        - insert(z): z is a key value for a new node, inserts a new node into tree
        - transplant: a helper function for delete method
        - delete(t.get_node(z)): z is a key, requires the user to call get_node() 
        - minimum(t.get_node(x)): x is a key, returns the minimum key value for the sub-trees of the input node,
            if called on the root, then it returns the minimum key for the whole BST
        - maximum(t.get_node(x)): x is a key, returns the maximum key value for the sub-trees of the input node,
            if called on the root, then it returns the maximum key for the whole BST
        - successor(t.get_node(x)): x is a key, returns the next largest key in the BST after the input node
        - predeccessor(t.get_node(x)): x is a key, returns the next smallest key in the BST before the input node
        - search(t.get_node(x),k): Takes x as the root and searches x's sub-trees for k. recusive.
            returns the key for a node if the node exists, else returns None
        - iterative_search(x,k): iterative version of search function
        - inorder_tree_walk(t.get_node(x)): Takes x as the root for a walk,
            returns an array of all BST elements sorted in ascending order
        """

    def __init__(self,root=None):
        self.root = root
        self.nodes = []
        self.walk = []

    def get_root(self):
        """ Return the root of the tree """
        return self.root

    def get_node(self,k):
        """ returns key for node k if k is in the BST, otherwise returns None """
        x = self.iterative_search(self.root,k)
        if x == None:
            return x
        else:
            return x

    def show_node(self,k):
        """ Prints out a node with both its left and right children """
        x = self.iterative_search(self.root,k)
        if x == None:
            print (x)
        else:
            print("Key = %s, l.child = %s, r.child = %s" % (x,x.left,x.right))

    def show_tree(self):
        """ Prints out each node in the tree, showing its children:
            l_child <- node -> r_child """
        for n in self.nodes:
            e = ""
            if n.key == None:
                continue
            if n.left != None:
                e += str(n.left) + " <- "
            else:
                e += "no child <- "
            e += str(n.key)
            if n.right != None:
                e += " -> " + str(n.right)
            else:
                e += " -> no child"
            print(e)

    def insert(self,z):
        """ Inserts a new node into the BST.
        Input is a node object
        Running time: O(h) on a BST of height h """

        y = None
        x = self.root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y    
        if y == None:
            self.root = z # tree was empty
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        self.nodes.append(z)

    def transplant(self,x,y):
        """ Replaces the sub-tree rooted at node x with the sub-tree
        rooted at node y, node x's parent becomes node y's parent, and
        node x's parent ends up having y as its appropriate child 
        
        Note: transplant does not update y.left and y.right, doing so or not 
        doing so its the responsibility of transplant's caller """
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        if y != None:
            y.parent = x.parent

    def delete(self,z):
        """ Input is the key for the node to be deleted.
        Requires a call to get_node() first,
        syntax:
            t.delete(get_node(z))
            where t is the name of the BST
            and z is the key for the node """

        # z = self.get_node(z)
        # Handles case where node z has no left child
        if z.left == None:
            self.transplant(z,z.right)

        # Handles case where node z has a left child but no right child
        elif z.right == None:
            self.transplant(z,z.left)
        
        else:
            y = self.minimum(z.right)
            if y.parent != z:
                self.transplant(y,y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z,y)
            y.left = z.left
            y.left.parent = y
        self.nodes.remove(z)

    def minimum(self,x):
        """ Return the node with the minimum key value in the tree 
        Running time: O(h) on a BST of height h """
        while x.left != None:
            x = x.left
        return x

    def maximum(self,x):
        """ Return the node with the maximum key value in the tree
        Running time: O(h) on a BST of height h """
        while x.right != None:
            x = x.right
        return x

    def successor(self,x):
        """ If all keys are distinct, the successor of a node x
        is the node with the smallest key greater than x.key.

        Returns the successor of node x in a BST if it exists,
        and None if x is the largest key in the tree 
        
        Running time: O(h) on a BST of height h """

        if x.right != None:
            return self.minimum(x.right)
        y = x.parent
        while y != None and x == y.right:
            x = y
            y = y.parent
        return y

    def predeccessor(self,x):
        """ If all keys are distinct, the predeccessor of a node x
        is the node with the largest key less than x.key.

        Returns the predeccessor of node x in a BST if it exists,
        and None if x is the smallest key in the tree 
        
        Running time: O(h) on a BST of height h """

        if x.left != None:
            return self.maximum(x.left)
        y = x.parent
        while y != None and x == y.left:
            x = y
            y = y.parent
        return y

    def search(self,x,k):
        """ recursive search 
        Input is x (the root) and k (a key)
        Returns k, if k is in the tree. Otherwise returns None 
        Running time: O(h) on a BST of height h """

        if x == None or k == x.key:
            return x
        if k < x.key:
            return self.search(x.left,k)
        else:
            return self.search(x.right,k)

    def iterative_search(self,x,k):
        """ iterative search 
        Input is x (the root) and k (a key)
        Returns k, if k is in the tree. Otherwise returns None
        Running time: O(h) on a BST of height h """

        while x != None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def inorder_tree_walk(self,x,walk=False):
        """ x is a node of the BST.
        Returns an array of with x and all the elements in x's sub-trees
        in ascending order
        get all elements in the BST by calling this function on the root 
        Running time: theta(n) linear """
        # Re-initializes self.walk as an empty array each time this function is called
        if not walk:
            self.walk = []
            walk=True
        if x != None:
            self.inorder_tree_walk(x.left,walk=True)
            # print(x.key) # uncomment for print only
            self.walk.append(int(x.key.__str__())) # comment this line for print only
            self.inorder_tree_walk(x.right,walk=True)
        return self.walk
    


####################### Methods Demonstration ####################### 

t = BST()
t.insert(node(3))
t.insert(node(2))
t.insert(node(7))
t.insert(node(5))
t.insert(node(1))
t.insert(node(9))
t.insert(node(8))

print(t.search(t.root,7)) # Output: 7, because key=7 is in BST

print(t.search(t.root,17)) # Output: None, because key=17 not in BST

print(t.maximum(t.root)) # Output: 9

print(t.minimum(t.root)) # Output: 1

print(t.get_root()) # Output: 3, because 3 was the first node inserted into BST

print(t.successor(t.root)) # Output: 5: because 5 is the largest value after 3 in the BST

print("Predeccessor is", t.predeccessor(t.root)) # Output: 1: because 1 is the smallest value after 3 in the BST

t.show_tree() # Output:
    # 2 <- 3 -> 7
    # 1 <- 2 -> no child
    # 5 <- 7 -> 9
    # no child <- 5 -> no child
    # no child <- 1 -> no child
    # 8 <- 9 -> no child
    # no child <- 8 -> no child

t.show_node(9) # Output: Key = 9, l.child = 8, r.child = None

print(t.inorder_tree_walk(t.root)) # Output: [1, 2, 3, 5, 7, 8, 9]

###### Deletion of node 1 #######
print()
t.delete(t.root.left)
print(t.inorder_tree_walk(t.root)) # [1, 3, 5, 7, 8, 9]

t.show_tree() # Output:
    # 1 <- 3 -> 7
    # 5 <- 7 -> 9
    # no child <- 5 -> no child
    # no child <- 1 -> no child
    # 8 <- 9 -> no child
    # no child <- 8 -> no child

###### Deletion of node 2 #######
print()
t.delete(t.get_node(9))
print(t.inorder_tree_walk(t.root)) # Output: [1, 3, 5, 7, 8]
t.show_tree() # Output:
    # 1 <- 3 -> 7
    # 5 <- 7 -> 8
    # no child <- 5 -> no child
    # no child <- 1 -> no child
    # no child <- 8 -> no child

print(t.maximum(t.root)) # Output: 8