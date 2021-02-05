'''
查询复杂度、构造复杂度和删除复杂度的分析可知，三种操作的时间复杂度皆为 O(log_2 n)~O(n)。下面分析线性结构的三种操作复杂度，以二分法为例：

查询复杂度，时间复杂度为 O(log_2 n)，优于二叉搜索树；
元素的插入操作包括两个步骤，查询和插入。查询的复杂度已知，插入后调整元素位置的复杂度为 O(n)，即单个元素的构造复杂度为：O(n)
删除操作也包括两个步骤，查询和删除，查询的复杂度已知，删除后调整元素位置的复杂度为 O(n)，即单个元素的删除复杂度为：O(n)
'''

class Node:
	def __init__(self,val,left=None,right=None):
		self.val=val
		self.left=left
		self.right=right

#Tree definition
class BSTree:
	def __init__(self,root=None):
		self.root=root	
	

	def traversal(self):
		traversal(self.root)

	def insert(self,value):
		self.root=insert(self.root,value)

	def search(self,value):
		node=search(self.root,value)
		print('searched ',node)
		return node 

	def delete(self,value):
		self.root=delete(self.root,value)


def traversal(root):
	#inorder Traversal
	if not root:
		return

	traversal(root.left)
	print(root.val,end=' ')
	traversal(root.right)


def insert(root,value):
	if not root:
		return Node(value)
	
	if value<root.val:
		root.left=insert(root.left,value)
	elif value>root.val:
		root.right=insert(root.right,value)

	return root


def delete(root,value):
	if not root:
		return None
	
	if value<root.val:
		root.left=delete(root.left,value)
	elif value>root.val:
		root.right=delete(root.right,value)
	else:
		#delete current node
		#put the largest leftnode here
		if root.left and root.right:#degree=2
			target=root.left
			while target.right:
				target=target.right
			root=delete(root,target.val)
			root.val=target.val

		else: #degree=[0/1]
			root=root.left if root.left else root.right
	return root


def search(root,value):
	if not root:
		return None
	
	if value==root:
		return root
	elif value<root.val:
		root.left=search(root.left,value)
	else:
		root.right=search(root.right,value)
	return root


if __name__=="__main__":
	arr = [5, 3, 4, 0, 2, 1, 8, 6, 9, 7]
	BST=BSTree()
	for v in arr:
		BST.insert(v)
	print(BST)
	print("InorderTraversal BSTree: ")
	BST.traversal()
	print('\n search: ')
	BST.search(4)

	for v in arr:
		print('after delete ',v,end=', BST is= ')
		BST.delete(v)
		BST.traversal()
		print()
	
