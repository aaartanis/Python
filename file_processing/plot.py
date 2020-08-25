import re
import os
import matplotlib.pyplot as plt
import numpy as np

def Plot_dir_File(path):

    #root指正在遍历这个文件夹本身的地址，dirs该文件夹中所有的目录的名字(不含子目录)
    #files是该文件夹中所有的文件（不包括子目录）
    for root,dirs,files in os.walk(path):
        maximum=0
        list_a=[]
        list_b=[]
        
        for each_path in files:
            file_path=os.path.join(root,each_path)
            data=np.loadtxt(file_path)
            list_a=data[:,0]
            list_b=data[:,1]
            b=max(list_b)
            maximum=max(maximum,b)
            
        for each_path in files:
            file_path=os.path.join(root,each_path)
            print(file_path)
            data=np.loadtxt(file_path)
            #使用plot绘制线条，第一个参数是第一列数据，第二个参数是第二列数据
            list_a=data[:,0]
            list_b=data[:,1]
            plt.plot(list_a,list(map(lambda x:x/maximum,list_b)))
    
path=r"C:/Users/Artanis/Desktop/yby/Nano/Nano1-T1"
Plot_dir_File(path)

#添加文本#X轴文本
plt.xlabel('time/ms')
#Y轴文本
plt.ylabel('intensity/%')
#标题
plt.title('title')
#指定文件名.jpg格式保存
plt.savefig('filename.jpg')
plt.show()


