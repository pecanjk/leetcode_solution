'''
给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。
'''

def findTheDifference(s:str,t:str)->str:
	hash_diff=[0]*26
	base=ord('a')
	for s_ in s:
		idx=ord(s_)-base
		hash_diff[idx]-=1
	for t_ in t:
		idx=ord(t_)-base
		hash_diff[idx]+=1

	diff=''
	for idx,v in enumerate(hash_diff):
		if v>0:
			diff+=chr(idx+base)
	return diff

if __name__=="__main__":
	s="abcd"
	t="abcde"
	out=findTheDifference(s,t)
	print(out)
	assert out=='e'
