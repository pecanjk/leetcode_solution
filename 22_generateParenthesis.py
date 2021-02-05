'''
括号生成

数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

'''

def generateParenthesis(n):
	result=[]
	backtracking(n,0,0,'',result)
	return result

def backtracking(n,left,right,s,result):
	if left<right:
		return
	
	if left==n and right==n:
		print('s ',s)
		result.append(s)
		return

	if left<n:
		backtracking(n,left+1,right,s+'(',result)
	
	if right<n:
		backtracking(n,left,right+1,s+')',result)

if __name__=="__main__":
	out=generateParenthesis(3)
	print(out)
