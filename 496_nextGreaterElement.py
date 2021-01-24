'''
给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。

请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。

nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。
'''
def nextGreaterElement(nums1:list,nums2:list)->list:
	hash_nG=dict()
	for idx,v in enumerate(nums2):
		i=idx+1
		stack=[v]
		res_idx=-1
		while i<len(nums2):
			if nums2[i]<v:
				stack.append(nums2[i])
				i+=1
			else:
				res_idx=i
				break
		if res_idx==-1:
			hash_nG[v]=res_idx
		else:
			hash_nG[v]=nums2[res_idx]

	print(hash_nG)
	result=[hash_nG[v] for v in nums1]
	return result


if __name__=="__main__":
	nums1=[137,59,92,122,52,131,79,236,94,171,141,86,169,199,248]
	nums2=[137,59,92,122,52,131,79,236,94,171,141,86,169,199,248]
	out=nextGreaterElement(nums1,nums2)
	print(out)

