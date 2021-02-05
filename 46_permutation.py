nums=[1,2,3]



#brutle
def permutation1(nums):
	possible=[]
	for i in nums:
		for j in nums:
			for k in nums:
				if len(set([i,j,k]))==3:
					possible.append([i,j,k])
	return possible	

def permute(nums):
	result=[]
	permutation2(nums,0,result)
	return result

#元素交换dfs
def permutation2(nums,left,result):
	if left==len(nums):
		result.append(nums[:])

	for idx in range(left,len(nums)):
		nums[idx],nums[left]=nums[left],nums[idx]
		permutation2(nums,left+1,result)
		nums[idx],nums[left]=nums[left],nums[idx]


def permute3(nums):
	result=[]
	permutation3(nums,len(nums),[],result)
	return result

#backtracking
def permutation3(nums,length,path,result):
	if len(path)==length:
		result.append(path[:])

	for i in range(len(nums)):
		if nums[i] not in path:
			path=path+[nums[i]]
			permutation3(nums,length,path,result)
			path.pop()


if __name__=="__main__":
	nums=[1,2,3]
	out=permutation1(nums)
	print(out)

	out=permute(nums)
	print('dfs swap ',out)

	out=permute3(nums)
	print('backtracking ',out)
