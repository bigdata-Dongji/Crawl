# encoding:utf8

s=input()
virus='_1234.exe'
time=s.count(virus,0,len(s))
print(time,end=' ')
_split=0
for i in range(time):
    position=s.index(virus)
    print(position+_split,end=' ')
    _split+=position+9
    s=s[position+9:]

