'''
反转一个单链表。
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
'''
class ListNode:
	def __init__(self,val,next=None):
		self.val=val
		self.next=next

def buildListNode(array):
	dummy=ListNode(0)
	head=ListNode(array[0])
	dummy.next=head
	for idx in range(1,len(array)):
		head.next=ListNode(array[idx])
		head=head.next
	return dummy.next

def printListNode(head:ListNode):
	while head:
		print(head.val,end='')
		head=head.next
	print()

def reverseList(head:ListNode)->ListNode:
	if not head or not head.next:
		return head

	p=reverseList(head.next) #This saves the last head node and return as reversedList head
	#when return back, do reverse
	head.next.next=head
	head.next=None

	return p
		

def reverseList2(head:ListNode)->ListNode:
	pre=None
	cur=head
	while cur:
		tmp=cur.next
		cur.next=pre
		pre=cur
		cur=tmp
	
	return pre

if __name__=="__main__":
	array=[1,2,3,4,5]
	head=buildListNode(array)
	printListNode(head)
	
	node=reverseList(head)
	print('1 reverse')
	printListNode(node)
	
	head=buildListNode(array)
	node=reverseList2(head)
	print('2 reverse')
	printListNode(node)
