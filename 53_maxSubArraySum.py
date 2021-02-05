'''
最大子序和

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
'''

def maxSubArray(nums):
	dp=[float('-inf')]*len(nums)
	dp[0]=nums[0]
	max_ans=nums[0]
	for i in range(1,len(nums)):
		dp[i]=max(nums[i],dp[i-1]+nums[i])
		max_ans=max(max_ans,dp[i])
		# print('dp ',dp)
	return max_ans

