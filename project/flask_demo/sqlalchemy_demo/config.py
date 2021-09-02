class Config():
    # 'mysql+pymysql://用户名称:密码@ip:端口/数据库名称'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/breach2020'
    # 动态追踪  用于设置数据发生变更之后是否发送信号给应用
    SQLALCHEMY_TRACK_MODIFICATIONS = False