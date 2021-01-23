'''
给定一个二叉树的根节点 root ，返回它的 中序 遍历
'''

class TreeNode:
	def __init__(self,val,left=None,right=None):
		self.val=val
		self.left=left
		self.right=right
	

def inorderTraversal(root:TreeNode)->list:
	vis=[]
	if root:
		vis+=inorderTraversal(root.left)
		vis.append(root)
    vis+=inorderTraversal(root.right)

	return vis
