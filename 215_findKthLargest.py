'''
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

'''
import heapq
def findKthLargest(nums:list,k:int)->int:
	nums_r=[-1*v for v in nums]
	heapq.heapify(nums_r)
	while k>1:
		heapq.heappop(nums_r)
		k-=1
	return -1*heapq.heappop(nums_r)

if __name__=="__main__":
	nums=[3,2,1,5,6,4]
	k=2
	out=findKthLargest(nums,k)
	print(out)
	assert out==5
