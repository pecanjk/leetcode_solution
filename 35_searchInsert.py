'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。你可以假设数组中无重复元素。
'''

def searchInsert(nums:list,target:int)->int:
	l,r=0,len(nums)-1
	while l<=r:
		mid_idx=l+(r-l)//2
		if nums[mid_idx]==target:
			return mid_idx
		elif nums[mid_idx]>target:
			r=mid_idx-1
		else:
			l=mid_idx+1
	return l

if __name__=="__main__":
	nums=[1,3,5,6]
	out=searchInsert(nums,2)
	print(out)
	assert out==1
