'''
Hamming Distance
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。

'''

def hammingDistance(x,y):
	dist=0
	while x or y:
		#get last bit 1/0
		bx=x&1
		by=y&1

		if bx!=by:
			dist+=1
		
		#bit right shift
		x=x>>1
		y=y>>1
	return dist


def hammingDistance2(x,y):
	dist=0
	#xor, then counts 1 can get the bin diff
	x=x^y
	while x:
		dist+=1
		x=x&(x-1)
	
	return dist 


if __name__=="__main__":
	x=1
	y=4
	out=hammingDistance(x,y)
	print('hamming distance ',out)
	
	out=hammingDistance2(x,y)
	print('hamming distance2 ',out)
