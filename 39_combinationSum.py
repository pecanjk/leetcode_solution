'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取


    所有数字（包括 target）都是正整数。
		    解集不能包含重复的组合。 

输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
[7],
[2,2,3]
]
'''

def combinationSum(nums,target):
	result=[]
	backtracking(nums,0,target,[],result)
	return result

def backtracking(nums,start,target,path,result):
	if target==0:
		result.append(path[:])
		return 
	if target<0:
		return

	for i in range(start,len(nums)):
		if target-nums[i]>=0:
			path=path+[nums[i]]
			backtracking(nums,i,target-nums[i],path,result)
			path.pop()


if __name__=="__main__":
	nums=[2,3,6,7]
	target=7
	out=combinationSum(nums,target)
	print(out)

