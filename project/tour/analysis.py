from pyecharts.charts import Bar,Line,Grid
from pyecharts import options as opts
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('data.csv',encoding='utf8',error_bad_lines=False)
data['dianping']=data['dianping'].str.replace('人','').astype(int)
data['percent']=data['percent'].astype(float)
top10=data.sort_values(by='dianping',ascending=False)[:6]
top10_tourist=top10['dianping'].values.tolist()
top10_percent=top10['percent'].values.tolist()
top10_name=top10['title'].values.tolist()
top10_name=[i[:7]+'..' for i in top10_name]
print(top10_tourist)
print(top10_percent)
print(top10_name)


line=(
    Line(init_opts=opts.InitOpts(width='2200px',height='1000px'))
    .add_xaxis(top10_name)
    .add_yaxis('',[10,20,30,40,50,60])
    .set_global_opts(title_opts=opts.TitleOpts(title='top6点评旅游项目的满意度',pos_left='center'),
                     xaxis_opts=opts.AxisOpts(name='旅游项目'),yaxis_opts=opts.AxisOpts(name='满意度（%）'))
)


line.render('result.html')



