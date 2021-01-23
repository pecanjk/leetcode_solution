'''
删除链表中等于给定值 val 的所有节点。
'''

class ListNode:
	def __init__(self,val,next=None):
		self.val=val
		self.next=next

def removeElements(head:ListNode,val:int)->ListNode:
	dummynode=ListNode(0,next=head)
	prenode=dummynode
	while head:
		if head.val==val:
			prenode.next=head.next
		else:
			prenode=prenode.next
		head=head.next
	return dummynode.next
