'''
子集

给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
'''

import copy
#dfs+ always append
def subsets(nums):
	result=[]
	findsubset(nums,0,[],result)
	return result

def findsubset(nums,start,path,result):
	result.append(copy.copy(path))
	
	if start==len(nums):
		return

	#dfs
	for idx in range(start,len(nums)):
		path=path+[nums[idx]]
		findsubset(nums,idx+1,path,result)
		path.pop()#撤销


#扩展法
def subsets2(nums):
	result=[[]]
	for i in range(len(nums)):
		result+=[sub+[nums[i]] for sub in result]
	return result


def subsets3(nums):
	result=[[]]
	#for every possible end, we need backtrack
	for end in range(1,len(nums)+1):
		findsubset3(nums,0,end,[],result)
	return result


#backtracking + 剪枝
def findsubset3(nums,start,end,path,result):
	if start==end:#this is 剪枝of backtracking
		result.append(copy.copy(path))
		return

	for i in range(start,len(nums)):
		path=path+[nums[i]]
		findsubset3(nums,i+1,end,path,result)
		path.pop()

if __name__=="__main__":
	nums=[1,2,3]
	out=subsets(nums)
	print('dfs all subsets ',out)

	out=subsets2(nums)
	print('expanding all subsets2 ',out)

	out=subsets3(nums)
	print('backtracking all subsets3 ',out)
