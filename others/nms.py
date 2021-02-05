'''
nms
'''


def NMS(dets,threshold):
	#This is very important to just sort index rather really sort dets
	score_idx=[(bbox[-1],idx) for idx,bbox in enumerate(dets)]	
	print(score_idx)
	score_idx.sort(key=lambda x: -x[0])
	print('after sort ',score_idx)
	result=[]
	while len(score_idx)>0:
		i=score_idx[0][1]#obtain the idx, always choose first largest score
		result.append(i)
		cur_bbox=dets[i][:4]
		iou_other_left=[]
		for other_score_idx,(_,idx_other) in enumerate(score_idx):
			other_bbox=dets[idx_other][:4]
			iou_other=iou(cur_bbox,other_bbox)
			print('iou_other ',iou_other)
			if iou_other<=threshold:
				iou_other_left.append(other_score_idx)
		
		#recollect score_idx that in other_score_idx, where iou<=threshold
		print('iou_other_left ',iou_other_left)
		score_idx=[score_idx[i] for i in iou_other_left]
		print('after ',score_idx)
	
	return result


def iou(box1,box2):
	area1=(box1[2]-box1[0])*(box1[1]-box1[3])
	area2=(box2[2]-box2[0])*(box2[1]-box2[3])
	
	xx1=max(box1[0],box2[0])
	yy1=min(box1[1],box2[1])
	xx2=min(box1[2],box2[2])
	yy2=max(box1[3],box2[3])

	#no inter then 0
	w=max(0,xx2-xx1)
	h=max(0,yy1-yy2)
	inter=w*h
	print('inter ',inter)
	
	return inter/(area1+area2-inter)


if __name__=="__main__":
	dets=[[210, 30, 280, 5, 0.6],
	      [120, 210, 240, 110, 1], 
				[70, 150, 260, 120, 0.8],
				[200, 180, 360, 140, 0.7]]

	threshold=0.1
	keep_idx=NMS(dets,threshold)
	print(keep_idx)
	
