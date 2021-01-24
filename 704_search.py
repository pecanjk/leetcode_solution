'''
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1
'''

def search(nums:list,target:int)->int:
	if not nums or len(nums)==0:
		return -1
	
	l,r=0,len(nums)-1
	while l<=r:
		mid_idx=l+(r-l)//2
		if nums[mid_idx]==target:
			return mid_idx
		elif nums[mid_idx]>target:
			r=mid_idx-1
		else:
			l=mid_idx+1
	
	return -1


if __name__=="__main__":
	nums=[-1,0,3,5,9,12]
	target=9
	out=search(nums,target)
	print(out)
	assert out==4

