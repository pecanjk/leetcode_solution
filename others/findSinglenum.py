'''
in a there is only one single
a=[1,3,2,1,2,3,5]
only 5 is single, find out it
'''
#hash_dict count
def findSingle(nums):
	hash_dict=dict()
	for v in nums:
		if v not in hash_dict:
			hash_dict[v]=1
		else:
			hash_dict[v]+=1
	
	for v,freq in hash_dict.items():
		if freq==1:
			return v
	return None

#bit &

def findSingle2(nums):
	v=nums[0]
	for i in range(1,len(nums)):
		v=v^nums[i]
	
	return v


if __name__=="__main__":
	nums=[1,3,2,1,2,3,5]
	out=findSingle(nums)
	print('out ',out)
	
	out=findSingle2(nums)
	print('& out ',out)


