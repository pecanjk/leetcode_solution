'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
'''

def moveZeros(nums:list):
	s,f=0,0
	while f<len(nums):
		if nums[f]!=0:
			nums[s]=nums[f]
			s+=1
		f+=1
	while s<len(nums):
		nums[s]=0
		s+=1

if __name__=="__main__":
	nums=[0,1,0,3,12]
	moveZeros(nums)
	print(nums)
