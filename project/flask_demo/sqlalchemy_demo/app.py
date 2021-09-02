from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
app = Flask(__name__)  # 创建Flask实例
db = SQLAlchemy(app)
# 导入类的方式导入flask配置
app.config.from_object(Config)

