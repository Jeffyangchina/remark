import sys#这个用来open文档中utf-8,而且文档目录必须是斜杠，windows
import json
entry={}
entry[0]='hello1'
entry[2]='hello3'
with open('C:/Users/XUEJW/Desktop/json.txt',mode='a',encoding='utf-8') as file:
	json.dump(entry,file,indent=2)#首行缩进2字节

