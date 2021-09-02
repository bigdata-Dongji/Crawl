import json,pymysql,requests,re
with open('01catch.txt',encoding='utf8')as f:
    data=f.readlines()


# def req(url):
#
#     headers={
#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
#     }
#     response=requests.get(url,headers=headers)
#     if response.status_code==200:
#         return response.content

db=pymysql.connect('localhost','root','root','my_movie_project')
cursor=db.cursor()
for i in data:
    i=json.loads(i)
    url=i.get('image')
    img_name='static/top100/'+re.findall('.*/(.*?.jpg)',url)[0]
    title=i.get('title')
    score=i.get('score')
    time=i.get('time').split('(')[0]

    sql="insert into top100 values(null,null,null,null,'{}',{},'{}',{},{},null,'{}',{},null,null,null,null,{})".format(title,score,img_name,0,0,time,0,80)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print(sql)


    # img=req(url)
    # with open(img_name,'wb')as f:
    #     f.write(img)