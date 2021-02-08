'''
totalHammingDistance

两个整数的 汉明距离 指的是这两个数字的二进制数对应位不同的数量。

计算一个数组中，任意两个数之间汉明距离的总和。

'''

def totalHammingDistance(nums):
	n=len(nums)
	total=0
	for i in range(32):
		cnt1=0
		# 统计每个数第i位上1的个数
		for num in nums:
			cnt1+=(num>>i)&1

		total+=cnt1*(n-cnt1)
	return total

if __name__=="__main__":
	nums=[4,14,2]
	out=totalHammingDistance(nums)
	print('total dist ',out)
