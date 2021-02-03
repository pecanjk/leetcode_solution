'''
fib
f(n)=f(n-1)+f(n-2)
'''

#递归
def fib(n):
	if n<2:
		return n
	
	return fib(n-1)+fib(n-2)

#递归
def fib1(n):
	if n<2:
		return n
	sum=fib1(n-1)+fib1(n-2)
	print('sum1',sum)
	return sum

#递归+memory
def fib2(n):
	mem=[-1]*(n+1)
	return helper(mem,n)

def helper(mem,n):
	if n<2:
		return n
	#已经计算过了
	if mem[n]!=-1:
		return mem[n]
	
	mem[n]=helper(mem,n-1)+helper(mem,n-2)
	return mem[n]


#动态规划
def fib3(n):
	if n<2:
		return n

	dp=[-1]*(n+1)
	dp[0]=0
	dp[1]=1
	for i in range(2,n+1):
		dp[i]=dp[i-1]+dp[i-2]
	
	return dp[n]

#动态规划+状态压缩
def fib4(n):
	if n<2:
		return n
	pre=0
	cur=1
	for i in range(2,n+1):
		sum_fib=cur+pre
		pre=cur
		cur=sum_fib
	
	return sum_fib

if __name__=="__main__":
	out=fib2(8)
	print('fib2(8) ',out)
	
	out=fib3(8)
	print('fib3(8) ',out)

	out=fib4(8)
	print('fib4(8) ',out)
