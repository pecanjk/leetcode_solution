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
	if root:
		vis.append(root)
		vis+=preorderTraversal(root.left)
    vis+=preorderTraversal(root.right)

	return vis
