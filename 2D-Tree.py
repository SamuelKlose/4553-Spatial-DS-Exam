import random

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None
	self.id = None
        
    def __repr__(self):
        return "< %s %s >" % (self.key,self.p)

    def __str__(self):
        return "< %s %s >" % (self.key,self.p)

class BinaryTree:
    def __init__(self, k = 2):
        self.root = None
        self.k = k
        self.discriminators = dict()
	self.numNodes = 0

    def length(self):
        return self.size

    def inorder(self, node):
        if node == None:
            return None
        else:
            self.inorder(node.left)
            print node.key,
            self.inorder(node.right)

    def search(self, k):
        print "Root:  Node Disc: "
	print self.root.key
	print self.getDisc(self.root)
	#print  self.root.key
        node = self.root
        while node != None:
            discVal = 0
            if node.key[(self.getDisc(node)+discVal)%self.k] == k[(self.getDisc(node)+discVal)%self.k]:
                if node.key == k:
                    print "Found Node: Node Disc:" 
		    print node.key
		    print self.getDisc(node)
                    return node
                else:
                    discVal = discVal + 1
            if node.key[(self.getDisc(node)+discVal)%self.k] > k[(self.getDisc(node)+discVal)%self.k]:
                node = node.left
            else:
                node = node.right
            print "Node Value: Node Disc:" 
	    print node.key
	    print self.getDisc(node)
        print "Could not find node"
        return None

    def minimum(self, node):
        x = None
        while node.left != None:
            x = node.left
            node = node.left
        return x

    def maximum(self, node):
        x = None
        while node.right != None:
            x = node.right
            node = node.right
        return x
        
    def nextDisc(self, i):
        return (i+1) % self.k
        
    def getDisc(self, node):
        return self.discriminators[node.id]

    def successor(self, node):
        parent = None
        if node.right != None:
            return self.minimum(node.right)
        parent = node.p
        while parent != None and node == parent.right:
            node = parent
            parent = parent.p
        return parent

    def predecessor(self, node):
        parent = None
        if node.left != None:
            return self.maximum(node.left)
        parent = node.p
        while parent != None and node == parent.left:
            node = parent
            parent = parent.p
        return parent

    def insert(self, k):
        t = TreeNode(k)
        parent = None
        node = self.root
        discLevel = 0
	self.numNodes = self.numNodes + 1
	t.id = self.numNodes
	self.discriminators[t.id] = discLevel
        while node != None:
            parent = node
            discLevel = self.nextDisc(discLevel)
            if node.key[discLevel] > t.key[discLevel]:
                node = node.left
            else:
                node = node.right
        t.p = parent
        self.discriminators[t.id] = discLevel
        if parent == None:
            t.left = None
            t.right = None
            self.root = t
        elif t.key[discLevel] < parent.key[discLevel]:
            parent.left = t
        else:
            parent.right = t
        return t


    def delete(self, node):
        if node.left == None:
            self.transplant(node, node.right)
        elif node.right == None:
            self.transplant(node, node.left)
        else:
            succ = self.minimum(node.right)
            if succ.p != node:
                self.transplant(succ, succ.right)
                succ.right = node.right
                succ.right.p = succ
            self.transplant(node, succ)
            succ.left = node.left
            succ.left.p = succ
        

    def transplant(self, node, newnode):
        if node.p == None:
            self.root = newnode
        elif node == node.p.left:
            node.p.left = newnode
        else:
            node.p.right = newnode
        if newnode != None:
            newnode.p = node.p
            
if __name__ == "__main__":

    B = BinaryTree();
    
    for i in range(100):
        B.insert([random.randint(1,100), random.randint(1, 100)])
    B.insert([11, 11])
    B.insert([22, 22])
    B.insert([33, 33])
    B.insert([44, 44])
    B.insert([55, 55])
    B.insert([66, 66])
    B.insert([77, 77])
    B.insert([88, 88])
    B.insert([99, 99])
    B.insert([100, 100])
    
    B.search([100, 100])
    """If I wanted to insert pairs of numbers"""
    """
    for i in range(10):
        for j in range(10):
            r1 = random.randint(1,100)
            r2 = random.randint(1,100)
            B.insert([r1,r2])
            print (r1,r2)
   """


