import json
from django.shortcuts import render
from django.views.generic.base import View
# from LcvSearch.search.models import ArticleType
from django.http import HttpResponse
from elasticsearch import Elasticsearch
from datetime import datetime
import redis

client = Elasticsearch(hosts=["127.0.0.1"])
redis_cli = redis.StrictRedis(decode_responses=True)

from elasticsearch_dsl import DocType, Date, Nested, Boolean, \
    analyzer, InnerObjectWrapper, Completion, Keyword, Text, Integer,Double
from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer
class CustomAnalyzer(_CustomAnalyzer):
    def get_analysis_definition(self):
        return {}
ik_analyzer = CustomAnalyzer("ik_max_word", filter=["lowercase"])
class ArticleType(DocType):
    # 猎云新闻类型
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
        index = "lieyun"
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

class IndexView(View):
    #首页
    def get(self, request):
        topn_search = redis_cli.zrevrangebyscore("search_keywords_set", "+inf", "-inf", start=0, num=5)
        return render(request, "index.html", {"topn_search":topn_search})

# Create your views here.
class SearchSuggest(View):
    def get(self, request):
        key_words = request.GET.get('s','')
        re_datas = []
        s_type = request.GET.get("s_type", "")
        if key_words:

            if s_type == 'info': # 信息披露
                s = XinpiType.search()
                s = s.suggest('my_suggest', key_words, completion={
                    "field": "suggest", "fuzzy": {
                        "fuzziness": 2
                    },
                    "size": 10
                })
                suggestions = s.execute_suggest()
                for match in suggestions.my_suggest[0].options:
                    source = match._source
                    re_datas.append(source["chi_name"])
            else:
                # 模糊搜索
                s = ArticleType.search()
                s = s.suggest('my_suggest', key_words, completion={
                    "field":"suggest", "fuzzy":{
                        "fuzziness":2
                    },
                    "size": 10
                })
                suggestions = s.execute_suggest()
                for match in suggestions.my_suggest[0].options:
                    source = match._source
                    re_datas.append(source["title"])
        return HttpResponse(json.dumps(re_datas), content_type="application/json")


class SearchView(View):
    def get(self, request):
        key_words = request.GET.get("q","")
        s_type = request.GET.get("s_type", "")
        if s_type == "info":
            index_name = "xinpi"
            source = "中国资本市场信息披露平台"

            redis_cli.zincrby("search_keywords_set", 1, key_words)

            topn_search = redis_cli.zrevrangebyscore("search_keywords_set", "+inf", "-inf", start=0, num=5)
            page = request.GET.get("p", "1")
            try:
                page = int(page)
            except:
                page = 1

            lieyun_count = redis_cli.get("lieyun_count")
            start_time = datetime.now()

            response = client.search(
                index="xinpi",
                body={
                    "query": {
                        "multi_match": {
                            "query": key_words,
                            "fields": ["chi_name", "indurstry","reg_addr","legal_repr"]
                        }
                    },
                    "from": (page - 1) * 10,
                    "size": 10,
                    "highlight": {
                        "pre_tags": ['<span class="keyWord">'],
                        "post_tags": ['</span>'],
                        "fields": {
                            "chi_name": {},
                            "indurstry": {},
                        }
                    }
                }
            )

            end_time = datetime.now()
            last_seconds = (end_time - start_time).total_seconds()
            total_nums = response["hits"]["total"]
            if (page % 10) > 0:
                page_nums = int(total_nums / 10) + 1
            else:
                page_nums = int(total_nums / 10)
            hit_list = []
            for hit in response["hits"]["hits"]:
                from collections import defaultdict
                hit_dict = defaultdict(str)
                if "highlight" not in hit:
                    hit["highlight"] = {}
                if "chi_name" in hit["highlight"]:  # 标题
                    hit_dict["title"] = "".join(hit["highlight"]["chi_name"])
                else:
                    hit_dict["title"] = hit["_source"]["chi_name"]

                if "legal_repr" in hit["highlight"]:  # 法人代表
                    hit_dict["legal_repr"] = '法人代表：'+"".join(hit["highlight"]["legal_repr"])
                else:
                    hit_dict["legal_repr"] = '法人代表：'+hit["_source"]["legal_repr"]

                if "email" in hit["highlight"]:  # 邮箱
                    hit_dict["email"] = '电子邮箱：'+"".join(hit["highlight"]["email"])
                else:
                    hit_dict["email"] = '电子邮箱：'+hit["_source"]["email"]

                if "reg_addr" in hit["highlight"]:  # 地址
                    hit_dict["address"] = "".join(hit["highlight"]["reg_addr"])
                else:
                    hit_dict["address"] = hit["_source"]["reg_addr"]

                if "operating_revenue" in hit["highlight"]:  # 地址
                    hit_dict["operating_revenue"] = '营业收入：'+"".join(hit["highlight"]["operating_revenue"])
                else:
                    if eval(hit["_source"]["operating_revenue"])>10000:
                        hit_dict["operating_revenue"] = '营业收入：'+str(round(eval(hit["_source"]["operating_revenue"])/10000,1))+' 万'


                if index_name == "xinpi":
                    if "indurstry" in hit["highlight"]:
                        hit_dict["indurstry"] = "".join(hit["highlight"]["indurstry"])[:500]
                    else:
                        hit_dict["indurstry"] = hit["_source"]["indurstry"][:500]
                elif index_name == "xinpi":
                    if "content" in hit["highlight"]:
                        hit_dict["content"] = "".join(hit["highlight"]["indurstry"])[:500]
                    else:
                        hit_dict["content"] = hit["_source"]["indurstry"][:500]

                if "report_date" in hit_dict:
                    hit_dict["create_date"] = hit["_source"]["report_date"]
                if "report_date" in hit["_source"]:
                    hit_dict["create_date"] = hit["_source"]["report_date"]
                hit_dict["email"] = hit["_source"]["email"]
                hit_dict["score"] = hit["_score"]

                hit_list.append(hit_dict)

            return render(request, "result.html", {"page": page,
                                                   "all_hits": hit_list,
                                                   "key_words": key_words,
                                                   "total_nums": total_nums,
                                                   "page_nums": page_nums,
                                                   "source": source,
                                                   "s_type": s_type,
                                                   "index_name": index_name,
                                                   "last_seconds": last_seconds,
                                                   "lieyun_count": lieyun_count,
                                                   "topn_search": topn_search})



# --------------------------------------------------------------------------------------------
        else:
            index_name = "lieyun"
            source = "猎云网"


        if s_type == "question":
            index_name = "zhihu"
            source = "知乎"

        redis_cli.zincrby("search_keywords_set", 1, key_words)

        topn_search = redis_cli.zrevrangebyscore("search_keywords_set", "+inf", "-inf", start=0, num=5)
        page = request.GET.get("p", "1")
        try:
            page = int(page)
        except:
            page = 1

        lieyun_count = redis_cli.get("lieyun_count")
        start_time = datetime.now()

        response = client.search(
            index= index_name,
            body={
                "query":{
                    "multi_match":{
                        "query":key_words,
                        "fields":["tags", "title", "content", "job_desc"]
                    }
                },
                "from":(page-1)*10,
                "size":10,
                "highlight": {
                    "pre_tags": ['<span class="keyWord">'],
                    "post_tags": ['</span>'],
                    "fields": {
                        "title": {},
                        "content": {},

                    }
                }
            }
        )

        end_time = datetime.now()
        last_seconds = (end_time-start_time).total_seconds()
        total_nums = response["hits"]["total"]
        if (page%10) > 0:
            page_nums = int(total_nums/10) +1
        else:
            page_nums = int(total_nums/10)
        hit_list = []
        for hit in response["hits"]["hits"]:
            from collections import defaultdict
            hit_dict = defaultdict(str)
            if "highlight" not in hit:
                hit["highlight"] = {}
            if "title" in hit["highlight"]:
                hit_dict["title"] = "".join(hit["highlight"]["title"])
            else:
                hit_dict["title"] = hit["_source"]["title"]

            if index_name == "xinpi":
                if "job_desc" in hit["highlight"]:
                    hit_dict["content"] = "".join(hit["highlight"]["job_desc"])[:500]
                else:
                    hit_dict["content"] = hit["_source"]["job_desc"][:500]
            elif index_name == "lieyun":
                if "content" in hit["highlight"]:
                    hit_dict["content"] = "".join(hit["highlight"]["content"])[:500]
                else:
                    hit_dict["content"] = hit["_source"]["content"][:500]

            if "create_date" in hit_dict:
                hit_dict["create_date"] = hit["_source"]["create_date"]
            if "create_date" in hit["_source"]:
                hit_dict["create_date"] = hit["_source"]["create_date"]
            hit_dict["url"] = hit["_source"]["url"]
            hit_dict["score"] = hit["_score"]

            hit_list.append(hit_dict)

        return render(request, "result.html", {"page":page,
                                               "all_hits":hit_list,
                                               "key_words":key_words,
                                               "total_nums":total_nums,
                                               "page_nums":page_nums,
                                               "source":source,
                                               "s_type":s_type,

                                               "index_name":index_name,
                                               "last_seconds":last_seconds,
                                               "lieyun_count":lieyun_count,
                                               "topn_search":topn_search})
