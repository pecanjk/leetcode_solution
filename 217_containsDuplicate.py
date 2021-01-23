'''
给定一个整数数组，判断是否存在重复元素。

如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
'''

def containsDuplicate(nums:list)->bool:
	hash_dict=dict()
	dup=False
	for v in nums:
		if v in hash_dict:
			hash_dict[v]+=1
			dup=True
			break
		else:
			hash_dict[v]=1
	return dup

