'''
给一非空的单词列表，返回前 k 个出现次数最多的单词。

返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。
'''

def topKFrequent(words:list,k:int)->list:
	hash_dict=dict()
	for w in words:
		if w in hash_dict:
			hash_dict[w]+=1
		else:
			hash_dict[w]=1
	
	hash_freq_dict=dict()
	for w,freq in hash_dict.items():
		if freq in hash_freq_dict:
			hash_freq_dict[freq].append(w)
		else:
			hash_freq_dict[freq]=[w]

	freq_list=list(hash_freq_dict.keys())
	freq_list.sort(reverse=True)
	print('freq_list',freq_list)

	idx=0
	result=[]
	while idx<len(freq_list):
		freq=freq_list[idx]
		tmp_list=hash_freq_dict[freq]
		tmp_list.sort()
		if len(result)+len(tmp_list)<=k:
			result+=tmp_list
		else:
			break
		idx+=1
	
	for v in tmp_list[:k-len(result)]:
		result.append(v)
	return result

if __name__=="__main__":
	words=["i", "love", "leetcode", "i", "love", "coding"]
	k=2
	out=topKFrequent(words,k)
	print(out)
	assert out==["i","love"]
