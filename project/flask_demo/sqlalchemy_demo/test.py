from aca.t_2020.case.flask_demo.sqlalchemy_demo.models import Wealth

w=Wealth.query.order_by(Wealth.rank.desc()).all()
# l=[]
# for i in w:
#     l.append([i.rank,i.name])

result=[]
for i in w:
        result.append({'movie_name':i.rank,'boxoffice': i.name})
print(result)