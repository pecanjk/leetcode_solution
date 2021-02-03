#Ali GaoDe 1st meeting
#升序数组旋转后，寻找最小值的位置。
#如arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#左旋转4位后变成arr = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]，
#最小值1的位置是第7位

#为什么比较mid与right而不比较mid与left？
#具体原因前面已经分析过了，简单讲就是因为我们找最小值，要偏向左找，目标值右边的情况会比较简单，容易区分，所以比较mid与right而不比较mid与left。

def find_min_pos(arr):
	left,right=0,len(arr)-1
	while left<right:
		mid=(left+right)//2
		#print(left,mid,right)
		if arr[mid]>arr[right]:
			#right
			left=mid+1
		else:
			right=mid
	min_pos=left
	return min_pos


if __name__=="__main__":
	arr=[5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
	out=find_min_pos(arr)
	print(out)
