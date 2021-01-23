'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
'''

def isValid(s:str)->bool:
	if len(s)==0:
		return True
	stack=[]
	braket_dict={'(':')','[':']','{':'}'}
	i=0
	while i<len(s):
		if s[i] in braket_dict.keys():
			stack.append(s[i])
		else:
			if s[i]!=braket_dict[stack[-1]] or len(stack)==0:
				return False
			stack.pop()
				
		i+=1
	return len(stack)==0


if __name__=="__main__":
	s="()[]{}"
	out=isValid(s)
	print(out)
	assert out==True
