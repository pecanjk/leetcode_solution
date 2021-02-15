'''
倍增
a*k
'''

def mul(a,k):
	result=0
	while k>0:
		if k&1==1:
			result+=a
		a+=a
		k=k>>1
	return result



def mul2(a,k):
	result=0
	while k>0:
		cur=a
		factor=1
		while factor+factor<=k:
			factor+=factor
			cur+=cur
		k-=factor
		print('factor ',factor,', k',k)	
		result+=cur
	return result


if __name__=="__main__":
	a=30
	k=5
	out=mul(a,k)
	print('{}*{}='.format(a,k),out)

	out=mul2(a,k)
	print('{}*{}='.format(a,k),out)

