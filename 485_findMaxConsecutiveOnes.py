'''
给定一个二进制数组， 计算其中最大连续1的个数。
'''

def findMaxConsecutiveOnes(nums:list)->int:
	if not nums or len(nums)==0:
		return 0
	
	max_len=0
	tmp_len=0
	for v in nums:
		if v==1:
			tmp_len+=1
			max_len=max(tmp_len)
		else:
			tmp_len=0
	
	max_len=max(max_len,tmp_len)
	return max_len

			
			
