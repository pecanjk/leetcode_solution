'''
MergeSort
'''

def MergeSort(nums):
	out=MergeSub(nums,0,len(nums)-1)	
	return out

def MergeSub(nums,left,right):
	if left==right:
		return 

	mid=(left+right)//2 #mid=(left+right)>>1
	MergeSub(nums,left,mid)
	MergeSub(nums,mid+1,right)

	#merge two ordered array
	m=MergeSortedArray(nums,left,mid,right)
	
	return m


def MergeSortedArray(nums,left,mid,right):
	#copy nums to L and R
	L=[v for v in nums[left:mid+1]]
	R=[v for v in nums[mid+1:right+1]]
	print('L ',L,', R ',R)

	i=0
	j=0
	p=left
	#Then copy in order to origin nums[left,right+1]
	while p<len(L)+len(R):
		if i<len(L) and j<len(R):
			#if L[i:]<R[j:]: #list compare rather than L[i]<R[j]
			if L[i]<R[j]:
				nums[p]=L[i]
				i+=1
			else:
				nums[p]=R[j]
				j+=1
		elif i==len(L) and j<len(R):
			nums[p]=R[j]
			j+=1
		
		elif j==len(R) and i<len(L):
			nums[p]=L[i]
			i+=1

		p+=1
	
	return nums



if __name__=="__main__":
	nums=[4,3,5,2,2,9]
	out=MergeSort(nums)
	print('after sort ',out)


