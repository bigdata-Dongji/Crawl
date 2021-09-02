from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import os
app=Flask(__name__)
app.secret_key=os.urandom(24)
# 设置数据库连接  语法：'数据库+驱动://用户名:密码@ip:端口/数据库名' 或 '数据库://用户名:密码@ip:端口/数据库名'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@127.0.0.1:3306/breach2020'
# 将其设置为True时，每次请求结束后都会自动提交数据库中的变动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
# 动态追踪  用于设置数据发生变更之后是否发送信号给应用
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
# 查询时会显示原始SQL语句
# app.config['SQLALCHEMY_ECHO']=True
db=SQLAlchemy(app)

class Role(db.Model):
    __tablename__='tb_role'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255),unique=True)
    users=db.relationship('User',backref='role')

    def __repr__(self):
        # 可以让显示对象的时候更直观
        return 'Role object:name=%s'%self.name

class User(db.Model):
    __tablename__='tb_user'
    id=db.Column(db.Integer,primary_key=True) # primary_key主键是整型的话，会默认设置自增主键
    name=db.Column(db.String(333),unique=True)
    password=db.Column(db.String(333))
    role_id=db.Column(db.Integer,db.ForeignKey('tb_role.id'))

    def __repr__(self):
        # 可以让显示对象的时候更直观
        return 'User object:name=%s'%self.name

if __name__ == '__main__':
    db.drop_all() # 删除所有表
    db.create_all() # 创建所有表
    # 创建对象
    role1=Role(name='police')
    # 添加对象到数据库
    db.session.add(role1)
    # 提交修改到数据库
    db.session.commit()

    r2=Role(name='engineer')
    u1=User(name='Jack',password='123456',role_id=role1.id)
    u2=User(name='Helen',password='666666',role_id=role1.id)
    u3=User(name='Peter',password='999999',role_id=r2.id)
    # 添加多条数据
    db.session.add_all([r2,u1,u2,u3])
    db.session.commit()

    # 查询所有姓名
    li=db.session.query(User).all()
    for i in li:
        print(i.name)
    print('-' * 50)
    # 查询第1个姓名
    print(db.session.query(User).first().name)
    print('-'*50)
    # 查询第2个姓名的另一种方式
    print(db.session.query(User).get(2).name)
    print('-'*50)
    # 查询姓名为Helen的数据
    data=User.query.filter_by(name='Helen').first()
    print(data.password)
    data2=User.query.filter(User.name=='Helen').first() #这两条都用于查询姓名为Helen的数据，`filter_by`里面不能用`!= `还有`> <` 等等，所以`filter`用得更多,`filter_by`只能用`=`
    print(data2.password)
    print('-' * 50)
    print(User.query.count())   #查询有多少条数据

    print(User.query.all()[1:3]) #查询第二到第四条数据

    print(User.query.filter(db.and_(User.name.startswith("P"),User.name.endswith('r'))).all()[0].name) # 查询name以'P'开头，name以r结尾的姓名，与操作用and_，或用or_ ，非用not
    print('-' * 50)
    # 根据id降序排序
    print(User.query.order_by(User.id.desc()).all())
    print('offset','-' * 50)
    # offset 偏移，也可理解为跳过，步长的意思
    print(User.query.offset(2).all())
    print(User.query.offset(1).limit(1).all())
    print('group by', '-' * 50)
    print(User.query.group_by(User.role_id).all())
    print(db.session.query(User.role_id,func.count(User.role_id)).group_by(User.role_id).all())
    print('关联查询', '-' * 50)
    # 关联查询_通过外键 ，从role表查询user表
    ro=Role.query.get(1)
    print(ro.users)
    print(ro.users[0].name)
    us=User.query.get(1)
    print(us.role)
    print(us.role.name)

    print('修改', '-' * 50)
    # 修改 数据名字为Peter改为Mike
    peter=db.session.query(User).filter(User.name=='Peter').all()[0]
    print(peter.name)
    peter.name='Mike'
    db.session.commit()
    print(peter.name)

    # 使用update并同时修改多个值
    helen=db.session.query(User).filter(User.name=='Helen')
    print(helen.all())
    helen.update({'name':'Alice','password':'000888'})
    print(db.session.query(User).filter(User.name=='Alice').first().name)
    print(db.session.query(User).filter(User.name=='Alice').first().password)

    print('删除', '-' * 50)
    # 删除 数据名字为Jack的数据
    print(db.session.query(User).all())
    db.session.delete(db.session.query(User).filter(User.name=='Jack').all()[0])
    db.session.commit()
    print(db.session.query(User).all())