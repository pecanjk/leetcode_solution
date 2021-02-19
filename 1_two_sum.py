#给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
#你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
def twoSum(nums:list,target:int)->list:
  i,j=0,0
  while i<len(nums):
    j=i+1
    while j<len(nums):
      if nums[i]+nums[j]==target:
        return [i,j]
      j+=1
    i+=1


def twoSum2(nums,target):
	hash_dict=dict()
	for idx, v in enumerate(nums):
		pair=target-v
		if pair in hash_dict:
			return [hash_dict[pair],idx]
		else:
			hash_dict[v]=idx


if __name__=="__main__":
	nums=[2,7,11,15]
	out=twoSum(nums,9)
	print('out',out)

	out=twoSum2(nums,9)
	print('out2 ',out)
