'''
第 i 个人的体重为 people[i]，每艘船可以承载的最大重量为 limit。

每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。

返回载到每一个人所需的最小船数。(保证每个人都能被船载)。
'''

def numRescueBoats(people:list,limit:int)->int:
	people.sort()
	l,r=0,len(people)-1
	num_boats=0
	while l<=r:
		if people[r]+people[l]<=limit:
			l+=1
		num_boats+=1
		r-=1
	return num_boats 


if __name__=="__main__":
	people=[1,2]
	limit=3
	out=numRescueBoats(people,limit)
	print(out)
	assert out==1

