from datetime import datetime
from elasticsearch_dsl import DocType, Date, Nested, Boolean, \
    analyzer, InnerObjectWrapper, Completion,  Text, Integer,Keyword,Double

from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer
from elasticsearch_dsl.connections import connections
connections.create_connection(hosts=["localhost"])

class CustomAnalyzer(_CustomAnalyzer):# 避免搜索建议使用ik报错
    def get_analysis_definition(self):
        return {}
ik_analyzer = CustomAnalyzer("ik_max_word", filter=["lowercase"])

class ArticleType(DocType):
    # 猎云网新闻类型
    suggest = Completion(analyzer=ik_analyzer)
    title = Text(analyzer="ik_max_word")
    create_date = Date()
    url = Keyword()
    url_object_id = Keyword()
    front_image_url = Keyword()
    # front_image_path = Keyword()
    # praise_nums = Integer()
    # comment_nums = Integer()
    # fav_nums = Integer()
    tags = Text(analyzer="ik_max_word")
    content = Text(analyzer="ik_max_word")

    class Meta:
        index = "lieyun" # 值不能有大写字母
        doc_type = "article"

class XinpiType(DocType):
    #资本市场信息披露的信息
    suggest = Completion(analyzer=ik_analyzer)
    chi_name = Text(analyzer="ik_max_word")
    email=Keyword()
    indurstry=Text(analyzer="ik_max_word")
    reg_addr=Keyword()
    legal_repr=Keyword()
    general_manager=Keyword()
    report_date=Date()
    operating_revenue=Double()
    np_parent_company_owners=Double()
    index=Integer()

    class Meta:
        index = "xinpi"
        doc_type = "info"

if __name__ == "__main__":
    # ArticleType.init()
    XinpiType.init()