'''
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

    每行中的整数从左到右按升序排列。
		    每行的第一个整数大于前一行的最后一个整数。
'''

def searchMatrix(matrix,target:int)->bool:
	col_num=len(matrix[0])
	l,r=0,len(matrix)*col_num-1
	while l<=r:
		mid_idx=l+(r-l)//2
		row,col=mid_idx//col_num,mid_idx%col_num
		if matrix[row][col]==target:
			return True
		elif matrix[row][col]>target:
			r=mid_idx-1
		else:
			l=mid_idx+1
	return False
