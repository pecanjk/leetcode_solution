'''
两数相加

给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807
'''

class ListNode:
	def __init__(self,val,next=None):
		self.val=val
		self.next=next

def build_list(array):
	dummy=ListNode(0)
	node=dummy
	for v in array:
		node.next=ListNode(v)
		node=node.next
	return dummy.next

def printListNode(listnode):
	node=listnode
	while node:
		print(node.val,end='')
		node=node.next
	print()

def addTwoNumbersListNode(l1:ListNode,l2:ListNode)->ListNode:
	dummy=ListNode(0)
	cur=dummy
	carrier=0

	while l1 or l2:
		l1v=l1.val if l1 else 0
		l2v=l2.val if l2 else 0

		sum_=l1v+l2v+carrier

		if sum_>=10:
			sum_=sum_-10
			carrier=1
		else:
			carrier=0
		
		cur.next=ListNode(sum_)

		l1=l1.next if l1 else None
		l2=l2.next if l2 else None
		cur=cur.next
	
	if carrier>0:
		cur.next=ListNode(carrier)
	return dummy.next


if __name__=="__main__":
	l1=[2,4,3]
	l2=[5,6,4]
	
	l1=build_list(l1)
	l2=build_list(l2)
	printListNode(l1)
	printListNode(l2)

	out=addTwoNumbersListNode(l1,l2)
	print('out')
	printListNode(out)
