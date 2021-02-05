'''
a=[[2],[3,4],[6,5,7],[4,1,8,3]]

out=2+3+5+1=11
'''

def shotestPath(array):
	n=len(array)
	max_f=float("inf")
	dp=[[max_f]*n for _ in range(n)]
	dp[0][0]=array[0][0]
	for i in range(1,n):
		for j in range(0,i+1):
			if j>0:
				dp[i][j]=min(dp[i-1][j]+array[i][j],dp[i-1][j-1]+array[i][j])
			else:
				dp[i][0]=dp[i-1][0]+array[i][0]
	print('dp ',dp)
	return min(dp[-1])


if __name__=="__main__":
	array=[[2],[3,4],[6,5,7],[4,1,8,3]]
	out=shotestPath(array)
	print(out)
			

