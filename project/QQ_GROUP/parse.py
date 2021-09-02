from lxml import etree
import re
with open('2020match','r',encoding='utf8')as f:
    html=f.read()
html=etree.HTML(html)
# html=etree.tostring(html)
# html=etree.parse(html,etree.HTMLParser())
school=html.xpath('//*[@class="td-card"]/span/text()')
sex=html.xpath('//*[@class="td-card"]/following::*[2]/text()')
school=[i.strip() for i in school]
sex=[i.strip() for i in sex]
school=[re.findall('.*职',i) for i in school]

import pandas as pd
school=pd.value_counts(school)


label=[]
for i in range(len(school.index)):
    if school.index[i]==[]:
        pass
    else:
        label.append(school.index[i][0])
nums=school.values
nums=list(nums)
nums.pop(0)
print(label)

# print(sex)