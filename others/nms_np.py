'''
nms
'''

import numpy as np

def NMS(dets,threshold):
	#x1、y1）（x2、y2）为box的左上和右下角标
	x1=dets[:,0]
	y1=dets[:,1]
	x2=dets[:,2]
	y2=dets[:,3]
	scores=dets[:,4]
	
	#areas of every bbox
	area=(x2-x1)*(y1-y2)
	print('area ',area)
	#sort the idx rather val
	order=scores.argsort()[::-1]#::-1 逆序
	print('order ',order)

	tmp=[]
	while order.size>0:
		i=order[0]
		tmp.append(i)#save the order idx
		#计算当前概率最大矩形框与其他矩形框的相交框的坐标
		# 由于numpy的broadcast机制，得到的是向量
		xx1=np.maximum(x1[i],x1[order[1:]])
		yy1=np.minimum(y1[i],y1[order[1:]])
		xx2=np.minimum(x2[i],x2[order[1:]])
		yy2=np.maximum(y2[i],y2[order[1:]])
		
		#计算相交框的面积,注意矩形框不相交时w或h算出来会是负数，需要用0代替
		w=np.maximum(0.0,xx2-xx1)
		h=np.maximum(0.0,yy1-yy2)
		inter=w*h
		#print('inter ',inter,inter.shape)
		#iou
		iou=inter/(area[i]+area[order[1:]]-inter)
		print('iou ',iou)
		
		#找到重叠度不高于阈值的矩形框索引
		idx=np.where(iou<=threshold)[0] #this idx is iou idx, 1 smaller than org dets
		#print('idx ',idx)

		#将order序列更新，由于前面得到的矩形框索引要比矩形框在原order序列中的索引小1，所以要把这个1加回来
		print('before ',order)
		order = order[idx+1]
		print('after order ',order)
	return tmp

if __name__=="__main__":
	dets = np.array([[210, 30, 280, 5, 0.6],
	                 [120, 210, 240, 110, 1],
                   [70, 150, 260, 120, 0.8],
									 [200, 180, 360, 140, 0.7]])

	threshold=0.1
	keep_dets=NMS(dets,threshold)

	print('keep_dets ',keep_dets)
	print(dets[keep_dets])
