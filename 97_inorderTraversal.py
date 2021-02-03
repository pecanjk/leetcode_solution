'''
给定一个二叉树的根节点 root ，返回它的 中序 遍历
'''

class TreeNode:
	def __init__(self,val,left=None,right=None):
		self.val=val
		self.left=left
		self.right=right
	

def inorderTraversal(root:TreeNode)->list:
	visit=[]
	inorder(root,visit)
	return visit

def inorder(node,visit)->list:
		if not node:
			return

		inorderTraversal(root.left,visit)
		visit.append(root)
    inorderTraversal(root.right,visit)


def inorderTravsersal2(root):
	visit=[]
	stack=[]
	while root or len(stack)>0:
		while root:
			stack.append(root)
			root=root.left

		if len(stack)>0:
			root=stack.pop()
			visit.append(root.val)
			root=root.right

	return visit
