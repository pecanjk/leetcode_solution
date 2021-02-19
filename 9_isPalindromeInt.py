'''
回文数

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。

输入：x = 121
输出：true

输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。
'''

def isPalindromeInt(num:int)->bool:
	if num<0 or (num!=0 and num%10==0):
		return False
	
	rev=0
	while num>rev:
		rev=rev*10+num%10
		num=num//10
	
	return rev==num or rev//10==num

if __name__=="__main__":
	x=121
	out=isPalindromeInt(x)
	print(x,out)

	x=1221
	out=isPalindromeInt(x)
	print(x,out)

