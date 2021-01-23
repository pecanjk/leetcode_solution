'''
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。
'''

def minSubArrayLen(s:int, nums:list)->int:
	l,r=0,0
	min_len=len(nums)+1
	sum_window=0
	while r<len(nums):
		sum_window+=nums[r]
		r+=1
		while sum_window>=s:
			min_len=min(min_len,r-l)
			sum_window=sum_window-nums[l]
			l+=1
	
	if min_len>len(nums):
		return 0
	else:
		return min_len

if __name__=="__main__":
	s=7
	nums=[2,3,1,2,4,3]
	out=minSubArrayLen(s,nums)
	print(out)
	assert out==2
