'''
 请实现有重复数字的升序数组的二分查找。
 输出在数组中第一个大于等于查找值的位置，如果数组中不存在这样的数，则输出数组长度加一

input 4,[1,2,4,4,5]
output 3
'''

def upper_bound(nums,target):
	n=len(nums)
	l,r=0,n-1
	while l<=r:
		mid=(l+r)//2
		if nums[mid]<target:
			l=mid+1
		elif nums[mid]==target:
			if mid==0 or nums[mid-1]!=target:
				return mid+1
			else:
				r=mid-1
		else:
			if mid==0 or nums[mid-1]<target:
				return mid+1
			else:
				r=mid-1
	return n+1

