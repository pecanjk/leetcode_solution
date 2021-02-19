'''
最长回文子串

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
'''

def longestPalindrome(s:str)->str:
	if not s or len(s)<2:
		return s
	
	n=len(s)
	max_length=1
	dp=[[False]*n for _ in range(n)]

	for i in range(n):
		dp[i][i]=True
	
	start=0
	for i in range(n-2,-1,-1):
		for j in range(i+1,n):
			if j-i<3:
				dp[i][j]=(s[i]==s[j])
			else:
				dp[i][j]=dp[i+1][j-1] and s[i]==s[j]
			
			if dp[i][j]:
				max_length=max(max_length,j-i+1)
				start=i

	return s[start:start+max_length]


if __name__=="__main__":
	s='babad'
	out=longestPalindrome(s)
	print('out ',out)


