#username - complete info
#id1      - 207768987
#name1    - Ella Bar 
#id2      - 212258990
#name2    - Lior Tsemah  


import random
import ArrayCreator
"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 
	
	@type key: int or None
	@param key: key of your node
	@type value: any
	@param value: data of your node
	"""
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		self.size = 0
		
	"""returns the key

	@rtype: int or None
	@returns: the key of self, None if the node is virtual
	"""
	def get_key(self):
		return self.key


	"""returns the value

	@rtype: any
	@returns: the value of self, None if the node is virtual
	"""
	def get_value(self):
		return self.value


	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)
	"""
	def get_left(self):
		return self.left


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	"""
	def get_right(self):
		return self.right


	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def get_parent(self):
		return self.parent


	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def get_height(self):
		return self.height


	"""returns the size of the subtree

	@rtype: int
	@returns: the size of the subtree of self, 0 if the node is virtual
	"""
	def get_size(self):
		return self.size


	"""sets key

	@type key: int or None
	@param key: key
	"""
	def set_key(self, key):
		self.key = key


	"""sets value

	@type value: any
	@param value: data
	"""
	def set_value(self, value):
		self.value = value


	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def set_left(self, node):
		self.left = node


	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def set_right(self, node):
		self.right = node


	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def set_parent(self, node):
		self.parent = node	

	def update_height(self):
		if self.is_real_node():
			prev = self.get_height()
			self.height = max(self.get_right().get_height(), self.get_left().get_height()) + 1
			return self.height - prev

	"""sets the height of the node

	@type h: int
	@param h: the height
	"""
	def set_height(self, h):
		self.height = h

	def update_size(self):
		if self.is_real_node():
			self.size = self.get_right().get_size() + self.get_left().get_size() + 1

	"""sets the size of node

	@type s: int
	@param s: the size
	"""
	def set_size(self, s):
		self.size = s
	
	def get_BF(self):
		if self.is_real_node:
			return self.get_left().get_height() - self.get_right().get_height()
		return 0

	#turns the node from virtual to real
	def realize(self, key, value): 
		self.set_key(key)
		self.set_value(value)
		self.set_height(0)
		self.set_size(1)
		self.set_right(AVLNode(None, None))
		self.get_right().set_parent(self)
		self.set_left(AVLNode(None, None))
		self.get_left().set_parent(self)


	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		return self.get_key() != None

	#performs a recursive in-order tour of the subtree
	def inorder(self, process_func, index):
		if self.is_real_node():
			index = self.get_left().inorder(process_func, index) + 1
			process_func(self, index)
			return self.get_right().inorder(process_func, index + 1)
		else:
			return index - 1

"""
A class implementing an AVL tree.
"""
class AVLTree(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.root = AVLNode(None, None)
		self.maximum = self.root

	"""
	searches for a node in the dictionary corresponding to the key
	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: node corresponding to key.
	"""    
	def search(self, key):
		def env_search(node, key):
			if (not node.is_real_node()):
				return None
			if (node.key == key):
				return node
			elif (key > node.key):
				return env_search(node.right, key)
			else:
				return env_search(node.left, key)
		return env_search(self.root, key)
	    
	#performs a left rotation centered on the given node
	def rotate_left(self, node):
		child = node.get_right()
		if (None != node.get_parent()):
			if node.get_parent().get_left() is node:
				node.get_parent().set_left(child)
			else:
				node.get_parent().set_right(child)
		else:
			self.root = child
		child.set_parent(node.get_parent())
		node.set_right(child.get_left())
		node.get_right().set_parent(node)
		child.set_left(node)
		node.set_parent(child)
		node.update_height()
		node.update_size()
		child.update_height()
		child.update_size()
	
	#performs a right rotation centered on the given node B
	def rotate_right(self, B):
		A=B.left
		B.left = A.right
		B.left.parent = B
		A.right = B
		A.parent = B.parent
		if (None == B.get_parent()):
			self.root = A
		else:
			if (B.get_parent().get_right() == B):
				B.get_parent().set_right(A)
			else:
				B.get_parent().set_left(A)
		B.parent = A
		B.update_size()
		B.update_height()
		A.update_size()
		A.update_height()
	
	#performs a left-right rotation centered on the given node and its left child
	def rotate_leftright(self, node):
		child = node.get_left()
		grand = child.get_right()
		if (None == node.get_parent()):
			self.root = grand
			grand.set_parent(None)
		else:
			grand.set_parent(node.get_parent())
			if (node.get_parent().get_left() == node):
				node.get_parent().set_left(grand)
			else:
				node.get_parent().set_right(grand)
		node.set_left(grand.get_right())
		node.get_left().set_parent(node)
		child.set_right(grand.get_left())
		child.get_right().set_parent(child)
		grand.set_right(node)
		node.set_parent(grand)
		grand.set_left(child)
		child.set_parent(grand)
		node.update_height()
		node.update_size()
		child.update_height()
		child.update_size()
		grand.update_height()
		grand.update_size()

	#performs a right-left rotation centered on the given node n and its right child
	def rotate_rightleft(self,n):
		c=n.right
		g=c.left
		p=n.parent
		g.parent=p
		c.left=g.right
		n.right=g.left
		c.left.parent=c
		n.right.parent=n
		g.right=c
		g.left=n
		n.parent=g
		c.parent=g
		if (None == p):
			self.root=g
		else:
			if (p.left==n):
				p.left=g
			else:
				p.right=g
		n.update_height()
		n.update_size()
		c.update_height()
		c.update_size()
		g.update_height()
		g.update_size()

	#performs the matching rotation to a node cur, if one is needed
	#uses the conditions laid out in the insert algorithm
	def perform_rotation(self, cur):
		balance_factor = cur.get_BF()
		if (balance_factor < -1): #bf == -2
			bf_right = cur.get_right().get_BF()
			if (-1 == bf_right):
				self.rotate_left(cur)
				return 1
			else:
				self.rotate_rightleft(cur)
				return 2
		elif (1 < balance_factor): #bf == 2
			bf_left = cur.get_left().get_BF()
			if (-1 == bf_left):
				self.rotate_leftright(cur)
				return 2 
			else:
				self.rotate_right(cur)
				return 1
		return 0

	#performs the matching rotation to a node cur, if one is needed
	#uses the conditions laid out in the delete algorithm
	#is also used in join, and thus in split too
	def perform_rotation_delete(self, cur):
		balance_factor = cur.get_BF()
		if (balance_factor < -1):
			bf_right = cur.get_right().get_BF()
			if (1 == bf_right):
				self.rotate_rightleft(cur)
				return 2
			else:
				self.rotate_left(cur)
				return 1
		elif (1 < balance_factor):
			bf_left = cur.get_left().get_BF()
			if (-1 == bf_left):
				self.rotate_leftright(cur)
				return 2 
			else:
				self.rotate_right(cur)
				return 1
			
		return 0

	#starts from node Cur and creates a new leaf using the BST insertion algorithm
	def create_node_bst(self, key, val, cur):
		while True:
			if (not cur.is_real_node()):
				cur.realize(key, val)
				if (self.maximum.is_real_node()):
					if (key > self.maximum.get_key()):
						self.maximum = cur
				else:
					self.maximum = cur
				return cur
			if (key < cur.get_key()):
				cur = cur.get_left()
			else:
				cur = cur.get_right()
	
	#finds the start point of a binary search using fingertree method
	#used to insert a node which is passed along to create_node_bst
	def find_start_fingertree(self, key):
		cur = self.maximum
		if (not cur.is_real_node()):
			return cur
		while (None != cur):
			if (cur.get_key() < key):
				return cur.get_right()
			cur = cur.get_parent()
		return self.root
		
	"""inserts val at position i in the dictionary	
		@type key: int
		@pre: key currently does not appear in the dictionary
		@param key: key of item that is to be inserted to self
		@type val: any
		@param val: the value of the item
		@rtype: int
		@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, key, val, use_finger = True):
		cur = None
		if (use_finger):
			start = self.find_start_fingertree(key)
			cur = self.create_node_bst(key, val, start)
		else:
			cur = self.create_node_bst(key, val, self.root)

		cur = cur.get_parent()
		fixes = 0
		checkRotation = True
		while (None != cur):
			cur.update_size()
			deltaHeight = cur.update_height()
			bf = cur.get_BF()
			if (checkRotation and abs(bf) < 2 and deltaHeight == 0):
				checkRotation = False #balancing is done; update size and height in parents and return
			if (checkRotation):
				balanceCost = self.perform_rotation(cur)
				if (0 == balanceCost):
					if (0 != deltaHeight):
						balanceCost = 1
				else:
					cur = cur.get_parent()
				fixes += balanceCost
			cur = cur.get_parent()
		return fixes

	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, node, balance = True):
		if (balance):
			if (node.get_key() == self.maximum.get_key()):
				self.maximum = self.predecessor(node)
		fixPoint = None
		count = 0
		if (not node.is_real_node()):
			return 0
		realLeft = node.get_left().is_real_node()
		realRight = node.get_right().is_real_node()
		if (not realLeft and not realRight):
			#node is a leaf, just remove it
			fixPoint = node.get_parent()
			if (fixPoint == None):
				#leaf was root, tree is now empty
				self.root = AVLNode(None, None)
				self.maximum = self.root
				return 0
			if (fixPoint.get_right().get_key() == node.get_key()):
				fixPoint.set_right(node.get_right())
				fixPoint.get_right().set_parent(fixPoint)
			else:
				fixPoint.set_left(node.get_right())
				fixPoint.get_left().set_parent(fixPoint)
			node.set_right(None)
			node.set_left(None)
			node.set_parent(None)
		elif (realLeft and not realRight):
			#node had left child but no right child, bypass and balance
			fixPoint = node.get_parent()
			if (fixPoint == None):
				self.root = node.get_left()
				node.set_left(None)
				self.root.set_parent(None)
				return 0
			if (fixPoint.get_right().get_key() == node.get_key()):
				fixPoint.set_right(node.get_left())
				fixPoint.get_right().set_parent(fixPoint)
			else:
				fixPoint.set_left(node.get_left())
				fixPoint.get_left().set_parent(fixPoint)
			node.set_right(None)
			node.set_left(None)
			node.set_parent(None)
		elif (realRight and not realLeft):
			#node had right child but no left child, bypass and balance
			fixPoint = node.get_parent()
			if (fixPoint == None):
				self.root = node.get_right()
				node.set_left(None)
				self.root.set_parent(None)
				return 0
			if (fixPoint.get_right().get_key() == node.get_key()):
				fixPoint.set_right(node.get_right())
				fixPoint.get_right().set_parent(fixPoint)
			else:
				fixPoint.set_left(node.get_right())
				fixPoint.get_left().set_parent(fixPoint)
			node.set_right(None)
			node.set_left(None)
			node.set_parent(None)
		else:
			#node had two children, replace with successor
			parent = node.get_parent()
			suc = self.successor(node)
			fixPoint = suc.get_parent()
			if (node == fixPoint): #successor is node's direct child 
				fixPoint = suc	   #so suc is the parent of the node actually removed
			self.delete(suc, False)
			if (None == parent):
				#deleted node was root
				self.root = suc
				suc.set_parent(None)
			else:
				if (parent.get_right().get_key() == node.get_key()):
					parent.set_right(suc)
				else:
					parent.set_left(suc)
				suc.set_parent(parent)
			suc.set_right(node.get_right())
			suc.get_right().set_parent(suc)
			node.set_right(None)
			suc.set_left(node.get_left())
			suc.get_left().set_parent(suc)
			node.set_left(None)
			node.set_parent(None)
		if (not balance):
			#occurs only when delete is called from inside itself
			return 0
		cur = fixPoint
		checkRotation = True 
		while (None != cur):
			cur.update_size()
			deltaHeight = cur.update_height()
			if (checkRotation and cur != fixPoint and abs(cur.get_BF()) < 2 and deltaHeight == 0):
				checkRotation = False
			if checkRotation:
				balanceCost = self.perform_rotation_delete(cur)
				if (0 == balanceCost):
					if (0 != deltaHeight):
						balanceCost = 1
				else:
					cur = cur.get_parent()
				count += balanceCost
			cur = cur.get_parent()
		return count
	
	#finds the next node, None if node is maximal
	def successor(self, node):
		if (node.get_right().is_real_node()):
			cur = node.get_right()
			while (cur.get_left().is_real_node()):
				cur  = cur.get_left()
			return cur
		else:
			cur = node.get_parent()
			while (True):
				if (None == cur):
					return None
				else:
					if (node.get_key() == cur.get_left().get_key()):
						return cur
					node = cur
					cur = node.get_parent()

	#finds the previous node, None if node is minimal
	def predecessor(self, node):
		if (node.get_left().is_real_node()):
			cur = node.get_left()
			while (cur.get_right().is_real_node()):
				cur  = cur.get_right()
			return cur
		else:
			cur = node.get_parent()
			while (True):
				if (None == cur):
					return None
				else:
					if (node.get_key() == cur.get_right().get_key()):
						return cur
					node = cur
					cur = node.get_parent()

	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		res = [None] * self.size()
		def process(node, index):
			res[index] = (node.get_key(), node.get_value())
		self.root.inorder(process, 0)
		return res

	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self):
		return self.get_root().get_size()	

	"""splits the dictionary at a given node

	@type node: AVLNode
	@pre: node is in self
	@param node: The intended node in the dictionary according to whom we split
	@rtype: list
	@returns: a list [left, right], where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""
	def split(self, node):
		def FindMaxima(left, right):
			#updated the maxima of the resulting trees so they are valid when returned
			if (right.root.is_real_node()):
				temp = right.root
				while (temp.get_right().is_real_node()):
					temp = temp.get_right()
				right.maximum = temp
			else:
				right.maximum = right.root
			if (left.root.is_real_node()):
				temp = left.root
				while (temp.get_right().is_real_node()):
					temp = temp.get_right()
				left.maximum = temp
			else:
				left.maximum = left.root
		parent = node.get_parent()
		left = AVLTree()
		left.root = node.get_left()
		left.root.set_parent(None)
		right = AVLTree()
		right.root = node.get_right()
		right.root.set_parent(None)
		if (None == parent):
			#split called on root, thus left, right subtrees are ready to be returned
			self.root = None
			self.maximum = None
			FindMaxima(left, right)
			return [left, right]
		while (None != parent):
			if (parent.get_right().get_key() == node.get_key()):
				#join left
				temp = AVLTree()
				temp.root = parent.get_left()
				temp.root.set_parent(None)
				left.join(temp, parent.get_key(), parent.get_value(), False)
			else:
				#join right
				temp = AVLTree()
				temp.root = parent.get_right()
				temp.root.set_parent(None)
				right.join(temp, parent.get_key(), parent.get_value(), False)
			node = parent
			parent = parent.get_parent()
		FindMaxima(left, right)
		self.root = self.maximum = None
		return [left, right]

	"""joins self with key and another AVLTree

	@type tree: AVLTree 
	@param tree: a dictionary to be joined with self
	@type key: int
	
	@param key: The key separting self with tree
	@type val: any 
	@param val: The value attached to key
	@pre: all keys in self are smaller than key and all keys in tree are larger than key,
	or the other way around.
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def join(self, tree, key, val, update_maximum = True):
		if (not tree.get_root().is_real_node()):
			#tree is empty, insert x into self
			retValue = self.get_root().get_height() + 2
			self.insert(key, val, False)
			return retValue
		if (not self.get_root().is_real_node()):
			#self is empty, insert x into tree and steal it
			retValue = tree.get_root().get_height() + 2
			tree.insert(key, val, False)
			self.root = tree.get_root()
			if (update_maximum):
				self.maximum = tree.maximum
			tree.root = None
			tree.maximum = None
			return retValue
		selfHeight = self.root.get_height()
		treeHeight = tree.root.get_height()
		treeHasLargerKeys = self.get_root().get_key() < key
		if(selfHeight == treeHeight):
			#trees are already of equal sizes; use x as new root
			x = AVLNode(key, val)
			x.set_right(tree.get_root() if treeHasLargerKeys else self.get_root())
			x.set_left(self.get_root() if treeHasLargerKeys else tree.get_root())
			x.get_right().set_parent(x)
			x.get_left().set_parent(x)
			self.root = x
			if (update_maximum):
				self.maximum = tree.maximum if treeHasLargerKeys else self.maximum
			tree.root = None
			tree.maximum = None
			x.update_height()
			x.update_size()
			return 1
		#t2 will be the taller tree; t1 will be the shorter tree
		t1 = None; t2 = None
		if (selfHeight < treeHeight):
			t1 = self
			t2 = tree
		else:
			t1 = tree
			t2 = self
		goLeft = t1.get_root().get_key() < t2.get_root().get_key()
		#find merge point
		b = t2.get_root()
		if (goLeft):
			while (b.get_height() > t1.get_root().get_height()):
				b = b.get_left()
		else:
			while (b.get_height() > t1.get_root().get_height()):
				b = b.get_right()
		x = AVLNode(None, None)
		x.realize(key, val)
		t1root = t1.get_root()
		self.root = t2.get_root()
		if (goLeft):
			x.set_left(t1root)
			x.set_right(b)
			x.set_parent(b.parent)
			x.parent.set_left(x)
			b.set_parent(x)
			t1root.set_parent(x)
			if (update_maximum):
				self.maximum = t2.maximum
			x.update_height()
			x.update_size()
			x = x.get_parent()
			while (None != x):
				x.update_height()
				x.update_size()
				self.perform_rotation_delete(x)
				x = x.get_parent()
		else:
			x.set_right(t1root)
			x.set_left(b)
			x.set_parent(b.parent)
			x.parent.set_right(x)
			b.set_parent(x)
			t1root.set_parent(x)
			if (update_maximum):
				self.maximum = t1.maximum
			x.update_height()
			x.update_size()
			x = x.get_parent()
			while (None != x):
				x.update_height()
				x.update_size()
				self.perform_rotation_delete(x)
				x = x.get_parent()
		tree.root = None
		tree.maximum = None
		return 1 + abs(selfHeight - treeHeight)

	"""compute the rank of node in the self

	@type node: AVLNode
	@pre: node is in self
	@param node: a node in the dictionary which we want to compute its rank
	@rtype: int
	@returns: the rank of node in self
	"""
	def rank(self, node):
		rank = 1
		cur = self.root
		key = node.get_key()
		curKey = cur.get_key() #root is real since node exists
		while (cur.get_key() != key):
			if (key < curKey):
				cur = cur.get_left()
				curKey = cur.get_key()
			else:
				rank += cur.get_left().get_size() + 1
				cur = cur.get_right()
				curKey = cur.get_key()
		# cur is node at this point
		return rank + cur.get_left().get_size()

	"""finds the i'th smallest item (according to keys) in self	
	@type i: int
	@pre: 1 <= i <= self.size()
	@param i: the rank to be selected in self
	@rtype: int
	@returns: the item of rank i in self
	"""
	def select(self, i):
		def select_recursive(node, i):
			if (not node.is_real_node()):
				return None
			left_subtree_rank = node.left.size if node.left is not None else 0
			r = 1 + left_subtree_rank
			if i == r:
				return node
			elif i < r:
				return select_recursive(node.left, i)
			else:
				return select_recursive(node.right, i-r)
		return select_recursive(self.root, i)

	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return self.root