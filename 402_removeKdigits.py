'''
nums='1432219'
k=3

1219
'''

def min_delete_k(nums,k):
	for i in range(1,k+1):
		print(i,nums)
		tmp_1=min_delete_1(nums)
		nums=str(tmp_1)
	print('final ',nums)
	return nums


def min_delete_1(nums):
	result=float('inf')
	for i in range(len(nums)):
		tmp=nums[0:i]+nums[i+1:]
		#print('tmp ',tmp)
		if tmp:
			tmp_int=int(tmp)
		else:
			tmp_int=0
		result=min(result,tmp_int)
		#print('result ',result)
	return result


#use an incremental stack to keep nums
def removeKdigits(nums,k):
	stack=[]
	remain=len(nums)-k
	for digit in nums:
		print('digit ',digit)
		print('stack ',stack)
		while k and stack and stack[-1]>digit:
			stack.pop()
			k-=1
		stack.append(digit)
	
	return ''.join(stack[:remain]).lstrip('0') or '0'



if __name__=="__main__":
	nums='1432219'
	k=3
	out=min_delete_k(nums,k)
	print(out)
	
	nums='10200'
	k=1
	out=min_delete_k(nums,k)
	print(out)


	nums='10'
	k=2
	out=min_delete_k(nums,k)
	print(out)

	
	nums='1003204'
	k=3
	out=min_delete_k(nums,k)
	print(out)

	nums='1432219'
	k=3
	out=removeKdigits(nums,k)
	print('stack remove out ',out)
