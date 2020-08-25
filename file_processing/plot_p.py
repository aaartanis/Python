import re
import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick

def Set_percent():
    fmt='%.f%%'
    yticks = mtick.FormatStrFormatter(fmt)
    plt.gca().yaxis.set_major_formatter(yticks)

def Plot_dir_File(sub_path):
    for root,dirs,files in os.walk(sub_path):
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
            print("This file is %s",file_path)
            data=np.loadtxt(file_path)
            #使用plot绘制线条，第一个参数是第一列数据，第二个参数是第二列数据
            list_a=data[:,0]
            list_b=data[:,1]
            plt.plot(list_a,list(map(lambda x:x*100/maximum,list_b)))

def Conf_save(title):
    plt.xlabel("time/ms")
    plt.ylabel("intensity")
    plt.title(title)
    Set_percent()
    plt.savefig(os.path.join(os.path.abspath("C:/Users/Artanis/Desktop/yby/figure"),title+'.jpg'))
    plt.cla()
        
    

def Search(path):
    for root,dirs,files in os.walk(path):
        for each_dirs in dirs:
            print(each_dirs)
            sub_path=os.path.join(root,each_dirs)
            Plot_dir_File(sub_path)
            Conf_save(each_dirs)

            

path=r"C:/Users/Artanis/Desktop/yby/Nano"
Search(path)
