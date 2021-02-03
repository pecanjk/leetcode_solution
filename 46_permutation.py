nums=[1,2,3]
possible=[]
for i in nums:
	for j in nums:
		for k in nums:
			if len(set([i,j,k]))==3:
				possible.append([i,j,k])

print(possible)


def permutation(nums,left=0):
	if left==len(nums):
		print(nums)
		result.append(nums[:])

	for idx in range(left,len(nums)):
		nums[idx],nums[left]=nums[left],nums[idx]
		permutation(nums,left+1)
		nums[idx],nums[left]=nums[left],nums[idx]

result=[]

permutation(nums,0)
print(result)
