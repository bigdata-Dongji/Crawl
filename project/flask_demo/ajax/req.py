# import requests,json
# data=requests.post('http://127.0.0.1:8080/total_boxoffice_data')
# jsonContent = json.loads(data.text)
# print(data.text)
# print(jsonContent)

# a = 0
# result = []
# for js in jsonContent:
#     result.append(js)
#     if js['movie_name'] == '八佰' and js['boxoffice'] == 309200.0:
#         a = a +1
# print(a)

b=[{'boxoffice': 13500.0, 'movie_name': '多力特的奇幻冒险'},
{'boxoffice': 18000.0, 'movie_name': '一点就到家'},
{'boxoffice': 25100.0, 'movie_name': '急先锋'},
{'boxoffice': 27700.0, 'movie_name': '花木兰'},
{'boxoffice': 45300.0, 'movie_name': '信条'},
{'boxoffice': 50500.0, 'movie_name': '我在时间尽头等你'},
{'boxoffice': 71800.0, 'movie_name': '夺冠'},
{'boxoffice': 147700.0, 'movie_name': '姜子牙'},
{'boxoffice': 225600.0, 'movie_name': '我和我的家乡'},
{'boxoffice': 309200.0, 'movie_name': '八佰'}]
c=[]
for i in b:
    c.append([i['boxoffice'],i['movie_name']])
print(c)