import pandas as pd
import os
file_dir=os.path.dirname(__file__)
csv_file=os.path.join(file_dir,'data','index.csv')

def query(str):
	#input data information
	str_len=len(str)
	str_case_list=[]
	img_file=[]
	#print(str_len)
	data=pd.read_csv(csv_file)
	#print(data[data['word']=='民'].ix[0,'index'])#loc,iloc,ix
	for i in range(str_len):
		if(str[i]=='\n'):
			continue
		var='%s'%str[i]
		#print(var)
		#print(data[data['word']=='%s'%str[i]].iloc[0,0])
		index=data[data['word']==var].iloc[0,0]
		#str_case_list.append(index)
		img_dir=os.path.join(file_dir,'data','%04d'%index)
		
		for dirPath, dirNames, fileNames in os.walk(img_dir):
			fileNames=str_num(fileNames)
			#print(fileNames)
			for file in fileNames:
				img_file.append(os.path.join(img_dir,'%s.jpg'%file))
				#img_file.append(os.path.join(img_dir,file))
	print(img_file)

	#return img_file  #img file path(order ascending)
def str_num(file_list):
	list_len=len(file_list)
	for i in range(list_len):
		file_list[i]=int(file_list[i][:-4])
	file_list.sort()
	return file_list

if __name__ == '__main__':
	query('槽落熏')