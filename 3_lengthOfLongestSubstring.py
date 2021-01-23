'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
'''
def lengthOfLongestSubstring(s:str)->int:
	if len(s)==0:
		return 0
	i,j=0,1
	while j<len(s):
		if s[j] in s[i:j] or len(set(s[i:j]))<j-i:
			i+=1

		j+=1
	
	return j-i

if __name__=="__main__":
	s = "abcabcbb"
	out=lengthOfLongestSubstring(s)
	print(out)
	assert out==3

	s = "bbbb"
	out=lengthOfLongestSubstring(s)
	print(out)
	assert out==1
