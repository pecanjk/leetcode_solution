'''
组合
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
'''

def combine(n,k):
	result=[]
	backtracking(n,1,k,[],result)
	return result

def backtracking(n,start,length,path,result):
	if len(path)==length:
		result.append(path[:])
		return
	
	for i in range(start,n+1):
		path=path+[i]
		backtracking(n,i+1,length,path,result)
		path.pop()
		
if __name__=="__main__":
	out=combine(4,2)
	print('n=4,k=2, combine ',out)
