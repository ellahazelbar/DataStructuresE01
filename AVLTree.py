#username - complete info
#id1      - 207768987
#name1    - Ella Bar 
#id2      - 212258990
#name2    - Lior Tsemah  



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
			self.height = max(self.get_right().get_height(), self.get_left().get_height()) + 1

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

	def realize(self, key, value, parent):
		self.set_key(key)
		self.set_value(value)
		self.set_parent(parent)
		self.set_height(0)
		self.set_size(1)
		self.set_right(AVLNode(None, None))
		self.set_left(AVLNode(None, None))


	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		return self.get_key() != None

	def inorder(self, process_func, index):
		if self.is_real_node():
			index = self.get_left().inorder(process_func) + 1
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
		# add your fields here



	"""searches for a node in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: node corresponding to key.
	"""
	def env_search(AVLNode, key):
		if (AVLNode.is_real_node()):
			return None
		if(AVLNode.key)==key:
			return AVLNode
		elif (key > AVLNode.key):
			return AVLTree.env_search(AVLNode.right,key)
		else:
			return AVLTree.env_search(AVLNode.left,key)
            
	def search(self, key):
		self.env_search(self.root, key)
	    
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

		
	def rotate_leftright(self, node):
		child = node.get_left()
		grand = child.get_right()
		if (None == node.get_parent()):
			self.root = grand
		else:
			grand.set_parent(node.get_parent())
			if (node.get_parent().get_left() == node):
				node.get_parent().set_left(grand)
			else:
				node.get_parent().set_right(grand)
		grand.set_parent(node.get_parent())
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

	def rotate_rightleft(self,n):
		nL=n.left
		c=n.right
		g=c.left
		cR=c.right
		p=n.parent
		g.parent=p
		c.left=g.right
		nL.right=g.left
		g.right.parent=c
		g.left.parent=nL
		g.right=nL
		g.left=n
		nL.parent=g
		n.parent=g
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


	"""inserts val at position i in the dictionary	
		@type key: int
		@pre: key currently does not appear in the dictionary
		@param key: key of item that is to be inserted to self
		@type val: any
		@param val: the value of the item
		@rtype: int
		@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, key, val):
		cur = self.root
		prev = None
		while True:
			if (not cur.is_real_node()):
				cur.realize(key, val, prev)
				break
			if (key < cur.get_key()):
				prev = cur
				cur = cur.get_left()
			else:
				prev = cur
				cur = cur.get_right()

		temp = cur.parent
		while temp != None:
			temp.update_height()
			temp = temp.get_parent()
		fixes = 0
		while (None != cur):
			balance_factor = cur.get_BF()
			if (balance_factor < -1):
				bf_right = cur.get_right().get_BF()
				if (-1 == bf_right):
					fixes += 1
					self.rotate_left(cur)
				else:
					fixes += 2
					self.rotate_rightleft(cur)
			elif (1 < balance_factor):
				bf_left = cur.get_left().get_BF()
				if (-1 == bf_left):
					fixes += 2 
					self.rotate_leftright(cur)
				else:
					fixes += 1
					self.rotate_right(cur)
			cur = cur.get_parent()
		return fixes

	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, node, balance = True):
		fixPoint = None
		count = 0
		if (not node.is_real_node()):
			return 0
		realLeft = node.get_left().is_real_node()
		realRight = node.get_right().is_real_node()
		if (not realLeft and not realRight):
			fixPoint = node.get_parent()
			if (fixPoint == None):
				self.root = None
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
			parent = node.get_parent()
			suc = self.successor(node)
			fixPoint = suc.get_parent()
			self.delete(suc, False)
			if (None == parent):
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
			suc.update_height()
			suc.update_size()
			node.set_left(None)
			node.set_parent(None)
		cur = fixPoint
		while cur != None:
			cur.update_height()
			cur.update_size()
			cur = cur.get_parent()

		if (not balance):
			return 0
		cur = fixPoint
		while (None != cur):
			balance_factor = cur.get_BF()
			if (balance_factor < -1):
				bf_right = cur.get_right().get_BF()
				if (1 == bf_right):
					count += 2
					self.rotate_rightleft(cur)
				else:
					count += 1
					self.rotate_left(cur)
			elif (1 < balance_factor):
				bf_left = cur.get_left().get_BF()
				if (-1 == bf_left):
					count += 2 
					self.rotate_leftright(cur)
				else:
					count += 1
					self.rotate_right(cur)
			cur = cur.get_parent()
		return count
	
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

		
	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		res = [None] * self.size()
		def process(node, index):
			res[index] = (node.get_key(), node.get_value())
		self.root.inorder(process)
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
		return None

	
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
	def join(self, tree, key, val):
		return None


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
			if (None == curKey): #cur is virtual - for internal testing
				return -1
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
			r= 1 + left_subtree_rank
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
	
t = AVLTree()
t.insert(6, 6)
t.insert(7, 7)
t.insert(8, 8)
t.insert(5, 5)
t.insert(4, 4)
t.insert(3, 3)
t.insert(2, 2)

print(t.delete(t.select(2)))