'''
给定一个二叉树的根节点 root ，返回它的 后序 遍历
'''

class TreeNode:
	def __init__(self,val,left=None,right=None):
		self.val=val
		self.left=left
		self.right=right
	

def postorderTraversal(root:TreeNode)->list:
	vis=[]
	if root:
		vis+=postorderTraversal(root.left)
    vis+=postorderTraversal(root.right)
		vis.append(root)
	return vis
