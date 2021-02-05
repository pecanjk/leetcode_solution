'''
反转字符串
输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
'''

def reverseString(s:list):
	if not s:
		return

	l,r=0,len(s)-1
	while l<r:
		s[l],s[r]=s[r],s[l]
		l+=1
		r-=1
	print('after reverse ',s)


def reverseString2(s:list):
	if not s:
		return
	reverse(s,0,len(s)-1)
	print('after reverse 2 ',s)
	
def reverse(s,left,right):
	if left>=right:
		return
	
	reverse(s,left+1,right-1)
	s[left],s[right]=s[right],s[left]


if __name__=="__main__":
	s=["h","e","l","l","o"]
	reverseString(s)

	s=["h","e","l","l","o"]
	reverseString2(s)
