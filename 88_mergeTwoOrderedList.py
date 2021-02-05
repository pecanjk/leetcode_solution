'''
合并两个有序数组
初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。

输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]

'''

def merge(nums1,m,nums2,n):
	while n>=1:
		if m>=1 and nums1[m-1]>nums2[n-1]:
			nums1[m+n-1]=nums1[m-1]
			m-=1
		else:
			nums1[m+n-1]=nums2[n-1]
			n-=1

	return nums1
	
if __name__=="__main__":
	nums1 = [1,2,3,0,0,0]
	m = 3
	nums2 = [2,5,6]
	n = 3

	out=merge(nums1,m,nums2,n)
	print(out)
