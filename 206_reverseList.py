'''
反转一个单链表。
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
'''
class ListNode:
	def __init__(self,val,next=None):
		self.val=val
		self.next=next

def reverseList(head:ListNode)->ListNode:
	if not head or not head.next:
		return head

	p=reverseList(head.next) #This saves the last head node and return as reversedList head
	#when return back, do reverse
	head.next.next=head
	head.next=None

	return p
		

