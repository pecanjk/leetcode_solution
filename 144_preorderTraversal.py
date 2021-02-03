'''
给定一个二叉树的根节点 root ，返回它的 前序 遍历
'''

class TreeNode:
	def __init__(self,val,left=None,right=None):
		self.val=val
		self.left=left
		self.right=right

def preorderTraversal(root:TreeNode)->list:
	vis=[]
	preorder(root,vis)
	return vis

def preorder(root:TreeNode,vis):
	if not root:
		return

	vis.append(root)
	preorderTraversal(root.left,vis)
  preorderTraversal(root.right,vis)


def preorderTraversal2(root):
	vis=[]
	stack=[]
	while root or len(stack)>0:
		while root:
			vis.append(root.val)
			stack.append(root)
			root=root.left

		if len(stack)>0:
			root=stack.pop()
			root=root.right

	return vis

