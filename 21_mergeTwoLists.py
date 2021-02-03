'''
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
'''

class ListNode:
	def __init__(self,val,next=None):
		self.val=val
		self.next=next
	
def mergeTwoList(l1:ListNode,l2:ListNode)->ListNode:
	if not l1:
		return l2
	if not l2:
		return l1
	if l1.val<=l2.val:
		l1.next=mergeTwoList(l1.next,l2)
		return l1
	else:
		l2.next=mergeTwoList(l1,l2.next)
		return l2
