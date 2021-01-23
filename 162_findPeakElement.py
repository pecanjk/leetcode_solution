'''
峰值元素是指其值大于左右相邻值的元素。

给你一个输入数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞ 。
'''

def findPeakElement(nums:list)->int:
	if len(nums)==1:
		return 0
	
	idx=0
	while idx+1<len(nums):
		if nums[idx]>nums[idx+1]:
			return idx
		idx+=1
	return len(nums)-1 

if __name__=="__main__":
	nums=[1,2]
	out=findPeakElement(nums)
	print('out ',out)
	assert out==1
