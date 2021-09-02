f=open('forward.txt','r')
data=f.readlines()
# for i in data:
#     print(i.replace('\n',''))
for i in range(0,len(data),2):
    # print(data[i].replace('\n','')+'=='+data[i+1].replace('\n',''))
    print(data[i].replace('\n',''))
f.close()
