# encoding:utf8
import os
path=os.getcwd() # 获取当前文件所在目录
for i in os.listdir(path): # 遍历目录所有文件
    # os.rename(i,i.replace('-','_'))
    # os.rename(i,i.replace('ff','f')) # 文件改名
    if os.path.isfile(i): # 判断是否是文件，而非目录
        print(i)
