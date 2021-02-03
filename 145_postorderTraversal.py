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
	postorder(root,vis)
	return vis

def postorder(root:TreeNode,vis)->list:
	if not root:
		return
	
	postorderTraversal(root.left,vis)
  postorderTraversal(root.right,vis)
	vis.append(root)


def postorderTraversal2(root):
	vis=[]
	stack=[]
	node=root
	lastvisited=node	
	while node or len(stack)>0:
		
		while node:
			stack.append(node)
			node=node.left
	#peek current stack top node
	node=stack[-1]
	if node.right is None or node.right==lastvisited:
		vis.append(node.val)
		stack.pop()
		lastvisited=node
		node=None
	else:
		node=node.right
	
	return vis

