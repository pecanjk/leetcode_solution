'''
多数元素
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素

输入：[2,2,1,1,1,2,2]
输出：2


尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
'''
def majorityElement(nums:list)->int:
	hash_dict=dict()
	max_counts=0

	for v in nums:
		if v not in hash_dict:
			hash_dict[v]=1
		else:
			hash_dict[v]+=1

		if hash_dict[v]>max_counts:
			max_counts=hash_dict[v]
		if max_counts>len(nums)/2:
			return v

#分治
def majorityElement2(nums):
	out=getMajorty(nums,0,len(nums)-1)
	return out

def getMajorty(nums,left,right):
	if left==right:
		return nums[left]

	mid=(left+right)//2
	left_major=getMajorty(nums,left,mid)
	right_major=getMajorty(nums,mid+1,right)

	if left_major==right_major:
		return left_major
	
	
	left_major_count=0
	right_major_count=0
	for v in nums[left:right+1]:
		if v==left_major:
			left_major_count+=1
		elif v==right_major:
			right_major_count+=1

	if left_major_count>len(nums)/2:
		return left_major
	else:
		return right_major




if __name__=="__main__":
	nums=[2,2,1,1,1,2,2]
	out=majorityElement(nums)
	print(out)

	out=majorityElement2(nums)
	print(out)
