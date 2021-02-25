'''
回文链表

请判断一个链表是否为回文链表。
输入: 1->2->2->1
输出: true
'''
class ListNode:
	def __init__(self,val,next=None):
		self.val=val
		self.next=next

def isPalindrome(head:ListNode):
	array=[]
	while head:
		array.append(head.val)
		head=head.next
	return array==array[::-1]
