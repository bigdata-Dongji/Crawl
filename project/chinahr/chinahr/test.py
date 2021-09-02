# encoding=utf8
from lxml import etree
a='''

<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no">
<meta name="theme-color" content="#000000">
<title>上海前端招聘网_上海前端招聘信息_上海前端工资-上海中华英才网</title>

<meta name="description" content="中华英才网上海前端招聘网,为您提供上海前端招聘信息,上海前端求职信息,上海前端工资待遇,同时您可了解上海前端岗位要求、岗位职责,公司介绍等信息。中华英才网是您招聘人才、找工作、求职、招工的理想选择！">

<meta name="keywords" content="上海前端招聘,上海前端招聘信息,上海前端工资,上海前端招聘网">    <script type="text/javascript">
    var _trackURL = "{'area':'2','channel':'','pagetype':'yingcailist','page':'searchlist','industry':'','job':'','salary':'','education':'','years':''}";
    var ____json4fe = {"catentry":[],"locallist":[{"dispid":"2","name":"上海","listname":"sh"}],"start":(new Date()).getTime(),"modules":"list"};
    ____json4fe.sid = '162471380210822682107543235';
</script>
<!--
<script type="text/javascript">
    document.domain = 'chinahr.com';
</script>
-->
<script type="text/javascript">
            var chindeed_zhuzhan_pc_tag='{"result":[{"ev":"1","ty":1,"el":".pc_search_ing","cl":"pc_search_ing"},{"ev":"1","ty":1,"el":".pc_search_confirm","cl":"pc_search_confirm"},{"ev":"1","ty":1,"el":".pc_search_workadress","cl":"pc_search_workadress"},{"ev":"1","ty":3,"el":".pc_search_workexp","em":{"0":"buxian","1":"yinianyixia","2":"1_2nian","3":"3_5nian","4":"6_7nian","5":"8_10nian","6":"shinianyishang"},"cl":"pc_search_workexp"},{"ev":"1","ty":3,"el":".pc_search_edu","em":{"0":"buxian","1":"dazhuan","2":"benke","3":"shuoshi","4":"bosohi"},"cl":"pc_search_edu"},{"ev":"1","ty":3,"el":".pc_search_salary","em":{"0":"buxian","1":"1000yixia","2":"1000","3":"2000","4":"3000","5":"5000","6":"8000","7":"12000","8":"20000","9":"25000"},"cl":"pc_search_salary"},{"ev":"1","ty":3,"el":".pc_search_worktype","em":{"0":"buxian","1":"quanzhizhaopin","2":"yingjiesheng"},"cl":"pc_search_worktype"},{"ev":"1","ty":1,"el":".pc_search_empty","cl":"pc_search_empty"}],"paramValues":{"psid":"162471380210822682107543235"},"tagGroupCode":"chindeed_zhuzhan_list_pc","state":1,"commonParams":"","version":1057148828236402688}';
        var statictagABtest='A';
</script>
<script type="text/javascript">
    var xxfwConfig = {namespace:'chinahr_zp_pclist'};
</script>
<script type="text/javascript" src="//j1.58cdn.com.cn/resource/xxzl/xxfw/xxfw.min_v20200907150609.js"></script>
<script>
    var _hmt = _hmt || [];
    (function() {
        var hm = document.createElement("script");
        hm.src = "https://hm.baidu.com/hm.js?42cc05139ef32c1de99099b0d3ac67c7";
        var s = document.getElementsByTagName("script")[0];
        s.parentNode.insertBefore(hm, s);
    })();
</script>
<script>
(function(){
    var bp = document.createElement('script');
    var curProtocol = window.location.protocol.split(':')[0];
    if (curProtocol === 'https') {
        bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
    }
    else {
        bp.src = 'http://push.zhanzhang.baidu.com/push.js';
    }
    var s = document.getElementsByTagName("script")[0];
    s.parentNode.insertBefore(bp, s);
})();
</script>
    <link rel="shortcut icon" href="//img.58cdn.com.cn/job/pc/chinahr/common/0.2/favicon.ico">


    <link rel="stylesheet" href="//c.58cdn.com.cn/git/hrg-fe-zhaopin-chinahr/chinahr-list-pc/style_v20201123150458.css">
    <link href="//c.58cdn.com.cn/git/hrg-fe-zhaopin-chinahr/chinahr-list-pc/static/css/main_v20201123150458.css" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="//c.58cdn.com.cn/componentsLoader/dist/CompontsLoader_v20201214135219.css">
    <!--[if IE 9]>
<style>
    .page-list{
        text-align: center;
    }
    .search-box-container > a{
        float: left;
        margin-top: 50px;
    }
    #citySelector{
        float: left;
        margin-top: 58px;
    }
    .search-box-wrap .search-box{
        float: left;
        margin-top:50px;
    }
    .net-police-wrap{
        width:1100px;
        margin: 0 auto;
        text-align: center;
    }
    #footer .footer_wrap:after{
        content:'';
        display:block;
        clear:both;
    }
    #footer .footer_left {
        float:left;
        margin-left:100px;
        margin-top:20px;
    }
    #footer .footer_main {
        float:left;
        margin-left:100px;
    }
    #footer .footer_main_row{
        float:left;
        margin-left:55px;
    }
    .totopbtn_block{
        text-align:center;
    }
    .fankui_block{
        text-align:center;
    }
    .label-text{
        line-height:43px;
    }
    .no-job{
        padding-top:150px;
        box-sizing:border-box;
    }
    .no-job img{
        display:block;
        margin: 0 auto;
    }
</style>
<![endif]-->


<!--[if lte IE 8]>
<script>window.location.href='http://support.dmeng.net/upgrade-your-browser.html?referrer='+encodeURIComponent(window.location.href);</script>
<![endif]-->

<!--[if lte IE 7]>
<script>window.location.href='http://support.dmeng.net/upgrade-your-browser.html?referrer='+encodeURIComponent(window.location.href);</script>
<![endif]-->
    <link rel="stylesheet" href="//c.58cdn.com.cn/job/pc/chinahr/common/0.2/commonBar_v20201123150147.css">
</head>

<body>
<!-- 发布职位 -->
<div class="layer_fabubtn"></div>

<!-- Topbar -->
<div id="commonTop"></div>
<div id="container">
    <div class="top">

        <div class="search-box-wrap">
            <div class="search-box-container">
                <!-- logo -->
                <a href="#">
    <span class="logo"></span>
</a>                <!-- 异步城市选择 -->
                <div id="citySelector"></div>
                <!-- 搜索框 -->
                <div class="search-box">
    <span class="search-icon"></span>
    <input type="text" name="search" placeholder="请输入职位名称或公司" maxlength='50' class="search-text" onclick="clickLog('from=pc_search_ing')" autocomplete="off">
    <input type="button" class="submit-btn" value="搜索工作机会" onclick="clickLog('from=pc_search_confirm')">

    <!-- 搜索联动 -->
    <div id="Search_linkage"></div>

    <!-- 清除浮动 -->
    <div class="clearfix"></div>

    <div id="search_hot"></div>

</div>            </div>
        </div>
        <div class="filter-select-box">
            <!-- 筛选条件 -->
            <div class="filter-box-warp">
    <div class="filter-box-container">
        <!--地点-->
        <div class="dropdown-wrap work-add">
    <span class="dropdown-select">
        <input ka="sel-exp" value="" class="ipt" readonly="">
        <span class="xialajiantou"></span>
        <div class="dropdown-menu">
            <ul>
                                <li  class="select" >
                    <a href="http://search.chinahr.com/sh/job/?key=%E5%89%8D%E7%AB%AF" class="pc_search_workadress">
                        全上海
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/pudongxinqu/job/?key=%E5%89%8D%E7%AB%AF" class="pc_search_workadress">
                        浦东
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/minxing/job/?key=%E5%89%8D%E7%AB%AF" class="pc_search_workadress">
                        闵行
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/songjiang/job/?key=%E5%89%8D%E7%AB%AF" class="pc_search_workadress">
                        松江
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/baoshan/job/?key=%E5%89%8D%E7%AB%AF" class="pc_search_workadress">
                        宝山
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/jiading/job/?key=%E5%89%8D%E7%AB%AF" class="pc_search_workadress">
                        嘉定
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/xuhui/job/?key=%E5%89%8D%E7%AB%AF" class="pc_search_workadress">
                        徐汇
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/qingpu/job/?key=%E5%89%8D%E7%AB%AF" class="pc_search_workadress">
                        青浦
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/jingan/job/?key=%E5%89%8D%E7%AB%AF" class="pc_search_workadress">
                        静安
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/putuo/job/?key=%E5%89%8D%E7%AB%AF" class="pc_search_workadress">
                        普陀
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/yangpu/job/?key=%E5%89%8D%E7%AB%AF" class="pc_search_workadress">
                        杨浦
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/fengxiansh/job/?key=%E5%89%8D%E7%AB%AF" class="pc_search_workadress">
                        奉贤
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/huangpu/job/?key=%E5%89%8D%E7%AB%AF" class="pc_search_workadress">
                        黄浦
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/hongkou/job/?key=%E5%89%8D%E7%AB%AF" class="pc_search_workadress">
                        虹口
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/changning/job/?key=%E5%89%8D%E7%AB%AF" class="pc_search_workadress">
                        长宁
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/jinshan/job/?key=%E5%89%8D%E7%AB%AF" class="pc_search_workadress">
                        金山
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/chongming/job/?key=%E5%89%8D%E7%AB%AF" class="pc_search_workadress">
                        崇明
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/shanghaizhoubian/job/?key=%E5%89%8D%E7%AB%AF" class="pc_search_workadress">
                        上海周边
                    </a>
                </li>
                            </ul>
        </div>
    </span>
</div>        <!--经验-->
        <div class="dropdown-wrap work-exp">
    <span class="dropdown-select">
        <input ka="sel-exp" value="" class="ipt" readonly="">
        <span class="xialajiantou"></span>
        <div class="dropdown-menu">
            <ul>
                                <li  class="select" >
                    <a href="http://search.chinahr.com/sh/job/?key=%E5%89%8D%E7%AB%AF" class="pc_search_workexp">
                        不限
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/sh/job/pve_5357_4/?key=%E5%89%8D%E7%AB%AF" class="pc_search_workexp">
                        1年以下
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/sh/job/pve_5357_5/?key=%E5%89%8D%E7%AB%AF" class="pc_search_workexp">
                        1-2年
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/sh/job/pve_5357_6/?key=%E5%89%8D%E7%AB%AF" class="pc_search_workexp">
                        3-5年
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/sh/job/pve_5357_7/?key=%E5%89%8D%E7%AB%AF" class="pc_search_workexp">
                        6-7年
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/sh/job/pve_5357_8/?key=%E5%89%8D%E7%AB%AF" class="pc_search_workexp">
                        8-10年
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/sh/job/pve_5357_9/?key=%E5%89%8D%E7%AB%AF" class="pc_search_workexp">
                        10年以上
                    </a>
                </li>
                            </ul>
        </div>
    </span>
</div>        <!--学历-->
        <div class="dropdown-wrap work-xueli">
    <span class="dropdown-select">
        <input ka="sel-exp" value="" class="ipt" readonly="">
        <span class="xialajiantou"></span>
        <div class="dropdown-menu">
            <ul>
                                <li  class="select" >
                    <a href="http://search.chinahr.com/sh/job/?key=%E5%89%8D%E7%AB%AF" class="pc_search_edu">
                        不限
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/sh/job/pve_5356_5/?key=%E5%89%8D%E7%AB%AF" class="pc_search_edu">
                        大专
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/sh/job/pve_5356_6/?key=%E5%89%8D%E7%AB%AF" class="pc_search_edu">
                        本科
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/sh/job/pve_5356_7/?key=%E5%89%8D%E7%AB%AF" class="pc_search_edu">
                        硕士
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/sh/job/pve_5356_8/?key=%E5%89%8D%E7%AB%AF" class="pc_search_edu">
                        博士
                    </a>
                </li>
                            </ul>
        </div>
    </span>
</div>        <!--薪资-->
        <div class="dropdown-wrap work-xinzi">
    <span class="dropdown-select">
        <input ka="sel-exp" value="" class="ipt" readonly="">
        <span class="xialajiantou"></span>
        <div class="dropdown-menu">
            <ul>
                                <li  class="select" >
                    <a href="http://search.chinahr.com/sh/job/?key=%E5%89%8D%E7%AB%AF" class="pc_search_salary">
                        不限
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/sh/job/?key=%E5%89%8D%E7%AB%AF&minxinzi=0_999" class="pc_search_salary">
                        1000元以下
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/sh/job/?key=%E5%89%8D%E7%AB%AF&minxinzi=1000_1999" class="pc_search_salary">
                        1000-2000元
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/sh/job/?key=%E5%89%8D%E7%AB%AF&minxinzi=2000_2999" class="pc_search_salary">
                        2000-3000元
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/sh/job/?key=%E5%89%8D%E7%AB%AF&minxinzi=3000_4999" class="pc_search_salary">
                        3000-5000元
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/sh/job/?key=%E5%89%8D%E7%AB%AF&minxinzi=5000_7999" class="pc_search_salary">
                        5000-8000元
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/sh/job/?key=%E5%89%8D%E7%AB%AF&minxinzi=8000_11999" class="pc_search_salary">
                        8000-12000元
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/sh/job/?key=%E5%89%8D%E7%AB%AF&minxinzi=12000_19999" class="pc_search_salary">
                        12000-20000元
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/sh/job/?key=%E5%89%8D%E7%AB%AF&minxinzi=20000_24999" class="pc_search_salary">
                        20000-25000元
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/sh/job/?key=%E5%89%8D%E7%AB%AF&minxinzi=25000_999999" class="pc_search_salary">
                        25000元以上
                    </a>
                </li>
                            </ul>
        </div>
    </span>
</div>        <!--工作类型-->
        <div class="dropdown-wrap work-type">
    <span class="dropdown-select">
        <input ka="sel-exp" value="" class="ipt" readonly="">
        <span class="xialajiantou"></span>
        <div class="dropdown-menu">
            <ul>
                                <li  class="select" >
                    <a href="http://search.chinahr.com/sh/job/?key=%E5%89%8D%E7%AB%AF" class="pc_search_worktype">
                        不限
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/sh/job/?key=%E5%89%8D%E7%AB%AF&worktype=1" class="pc_search_worktype">
                        全职招聘
                    </a>
                </li>
                                <li >
                    <a href="http://search.chinahr.com/sh/job/?key=%E5%89%8D%E7%AB%AF&worktype=2" class="pc_search_worktype">
                        应届生
                    </a>
                </li>
                            </ul>
        </div>
    </span>
</div>        <!--清空筛选-->
        <a class="clear-filter pc_search_empty" href="javascript:void(0)">
    <span class="clear-filter-img"></span>
    <span class="clear-filter-text">
        清空筛选条件
    </span>
</a>    </div>
</div>
        </div>
    </div>
    <div class="mian-page">
        <div class="main-page-wrap">
            <!-- 搜索结果 -->
            <p class="total-jobs">
    共为您找到
    <span>
                       2437
                    </span>
    条职位
</p>
            <!-- 搜索结果列表 -->
            <div class="job-list-box">
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/tech/42954020662421x.shtml">
        <ul class="l1">
            <li class="job-name" title="前端人员" data-info="42954020662421">
                前端人员
            </li>
            <li class="fabu-date">
                2020-07-24
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                8000-10000 元/月
            </li>
            <li class="job-address">
                上海-闵行-虹桥 | 经验不限 | 学历不限
                                    <span title='WEB前端开发'>
                        | WEB前端开发
                    </span>
                            </li>
            <li class="job-company" title='上海万物巨稀科技有限责任公司'>
                上海万物巨稀科技有限责任公司
            </li>
        </ul>
        <p class="l3">
            Web前端  HTML5Javascript CSS AngularJS 移动端 职位描述: 1.负责公司产品的包含PC端，移动端的开发，调试和维护;具备跨终端的前端开发能力 2.利用各种web技术进行前端页面制作和网站交互功能实现; 3.与后台工程师协作，进行WEB前端表现层及与前后端交互的设计和开发，完成数据交互、动态信息维护及展现; 4.参...
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>五险一金</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/tech/44160685323655x.shtml">
        <ul class="l1">
            <li class="job-name" title="前端开发" data-info="44160685323655">
                前端开发
            </li>
            <li class="fabu-date">
                2020-11-11
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                8000-12000 元/月
            </li>
            <li class="job-address">
                上海-浦东-源深 | 经验不限 | 本科
                                    <span title='WEB前端开发'>
                        | WEB前端开发
                    </span>
                            </li>
            <li class="job-company" title='上海汝点信息科技有限公司'>
                上海汝点信息科技有限公司
            </li>
        </ul>
        <p class="l3">
            前端开发工程师（Vue.js） 【工作职责】 1、主要负责公司应用前端网页的设计、适配、开发工作； 2、根据产品需求按时高质完成软件开发和维护工作，不断优化和提升用户体验； 3、和团队成员进行有效沟通协作，共同实现工作目标。 4、通过敏捷开发方式高质、高效地完成任务；考虑和兼顾用户体验、性能、可维护性等问题。 【任职条件】 1、本科及以上学历，二年以上前端/移动端的开发经验； 2、熟练掌握Vue...
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>周末双休</span>
                                                                                <span>年底双薪</span>
                                                                                <span>五险一金</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/tech/42754562065174x.shtml">
        <ul class="l1">
            <li class="job-name" title="Web前端" data-info="42754562065174">
                Web前端
            </li>
            <li class="fabu-date">
                2020-07-08
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                7000-10000 元/月
            </li>
            <li class="job-address">
                上海-青浦-华新 | 3-5年 | 大专
                                    <span title='WEB前端开发'>
                        | WEB前端开发
                    </span>
                            </li>
            <li class="job-company" title='火神（上海）网络科技有限公司'>
                火神（上海）网络科技有限公司
            </li>
        </ul>
        <p class="l3">
            完成Web前端应用、交互代码开发
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>周末双休</span>
                                                                                <span>五险一金</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/zhuanye/43450659689733x.shtml">
        <ul class="l1">
            <li class="job-name" title="教育前端销售" data-info="43450659689733">
                教育前端销售
            </li>
            <li class="fabu-date">
                2020-09-29
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                9000-18000 元/月
            </li>
            <li class="job-address">
                上海-徐汇-徐家汇 | 1年以下 | 大专
                                    <span title='招生/课程顾问'>
                        | 招生/课程顾问
                    </span>
                            </li>
            <li class="job-company" title='上海新田餐饮有限公司杨南路分公司'>
                上海新田餐饮有限公司杨南路分公司
            </li>
        </ul>
        <p class="l3">
            技能要求： 晚托教师 （一）主要工作职责： 1、管理学员作业和进行答疑及背默读，作业后跟进孩子个性化学习，如：雏鹰班（1年级）双师教学（录播＋跟进互动）；成长班（2/3/4年级）错题训练，名校加练和阶段复习等 ； 2、根据学生情况定期进行数据分析总结，与学生家长进行有效及时沟通，并建立长期、稳定、良好的信任关系，杜绝发生家长投诉； 3、为在读学生...
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>年底双薪</span>
                                                                                <span>五险一金</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/tech/44278564679451x.shtml">
        <ul class="l1">
            <li class="job-name" title="WEB前端开发" data-info="44278564679451">
                WEB前端开发
            </li>
            <li class="fabu-date">
                2020-12-17
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                薪资面议 
            </li>
            <li class="job-address">
                上海-浦东 | 1-2年 | 大专
                                    <span title='WEB前端开发'>
                        | WEB前端开发
                    </span>
                            </li>
            <li class="job-company" title='中民车联科技有限公司'>
                中民车联科技有限公司
            </li>
        </ul>
        <p class="l3">
            工作内容：要求离职状态可立即到岗！！ 职位要求： 1、有扎实的前端基础, 熟练掌握包括但不限于js/JQuery/nodejs/css/html/less/sass等前端技术，有3-5年的前端开发经验； 2、项目中熟练使用过React, Vue/Angular可作为加分项； 3、熟悉webpack的配置, 熟悉git操作，有处理浏览器兼容性的经验；<br ...
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>五险</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/tech/43295496599456x.shtml">
        <ul class="l1">
            <li class="job-name" title="web前端开发" data-info="43295496599456">
                web前端开发
            </li>
            <li class="fabu-date">
                2020-12-17
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                薪资面议 
            </li>
            <li class="job-address">
                上海-黄浦-老西门 | 经验不限 | 学历不限
                                    <span title='WEB前端开发'>
                        | WEB前端开发
                    </span>
                            </li>
            <li class="job-company" title='德州鲨云电子商务有限责任公司'>
                德州鲨云电子商务有限责任公司
            </li>
        </ul>
        <p class="l3">
            技能要求： Web前端，Vue，CSS，Javascript，HTML5，CSS3 1、专科及以上学历，计算机相关专业 2、1年以上web前端开发经验 3、熟练掌握 HTML、JS、ES6、CSS等基础知识 4、熟练掌握 Vue、React等常用框架，熟练组件化开发模式 5、熟悉npm、less、webpack、gulp、git等开发工...
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>周末双休</span>
                                                                                <span>五险一金</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/tech/44257869127312x.shtml">
        <ul class="l1">
            <li class="job-name" title="Java前端开发" data-info="44257869127312">
                Java前端开发
            </li>
            <li class="fabu-date">
                2020-12-20
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                4500-8000 元/月
            </li>
            <li class="job-address">
                上海-宝山 | 经验不限 | 大专
                                    <span title='WEB前端开发'>
                        | WEB前端开发
                    </span>
                            </li>
            <li class="job-company" title='上海誉骋文化传播有限公司'>
                上海誉骋文化传播有限公司
            </li>
        </ul>
        <p class="l3">
            Java基础知识扎实，熟悉spring Boot框架，熟悉MySQL数据库，逻辑清晰，接受能力强，工作经验一年左右,薪资 3-5K、可接受实习生  做五休二、早九晚六交社保
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>五险一金</span>
                                                                                <span>房补</span>
                                                                                <span>包吃</span>
                                                                                <span>包住</span>
                                                                                <span>加班补助</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/tech/43936702200834x.shtml">
        <ul class="l1">
            <li class="job-name" title="uni前端开发" data-info="43936702200834">
                uni前端开发
            </li>
            <li class="fabu-date">
                2020-12-02
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                8000-10000 元/月
            </li>
            <li class="job-address">
                上海-金山-金山新城 | 经验不限 | 学历不限
                                    <span title='WEB前端开发'>
                        | WEB前端开发
                    </span>
                            </li>
            <li class="job-company" title='上海奇旭网络科技有限公司'>
                上海奇旭网络科技有限公司
            </li>
        </ul>
        <p class="l3">
            岗位职责： 1、手机APP软件前端开发，使用UNI-APP技术； 2、根据产品需求，分析并给出前端解决方案; 3、改善用户体验与平台兼容性； 4、能独立进行常规的UI设计，组件开发； 5、能独立调试、打包、发布； 任职要求： • 具备使用uniapp跨平台输出iOS和Android应用能力 • 熟练掌握前端开发技术(...
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>五险一金</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/tech/43476425209636x.shtml">
        <ul class="l1">
            <li class="job-name" title="Web前端开发" data-info="43476425209636">
                Web前端开发
            </li>
            <li class="fabu-date">
                2020-09-09
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                10000-15000 元/月
            </li>
            <li class="job-address">
                上海-闵行-莘庄 | 经验不限 | 学历不限
                                    <span title='WEB前端开发'>
                        | WEB前端开发
                    </span>
                            </li>
            <li class="job-company" title='上海莫凡信息技术有限公司'>
                上海莫凡信息技术有限公司
            </li>
        </ul>
        <p class="l3">
            工作内容： 1) 负责Web前端页面开发，各类交互设计和实现； 2) 负责页面易用性改进和技术优化； 3) 根据总体设计完成软件的设计与开发工作； 4) 编写相关技术文档。   岗位要求： 1、本科以上学历，计算机相关专业，2年以上前端开发工作经验。 2、了解常见前端框架/库，如：AngularJS，React，Vue 3、熟练掌握H5、CSS3、ES6 4、有小程序项目经验的优先考虑 5、有团...
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>饭补</span>
                                                                                <span>交通补助</span>
                                                                                <span>环境好</span>
                                                                                <span>周末双休</span>
                                                                                <span>免费培训</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/tech/44533833991844x.shtml">
        <ul class="l1">
            <li class="job-name" title="Web前端开发工程师" data-info="44533833991844">
                Web前端开发工程师
            </li>
            <li class="fabu-date">
                2020-12-14
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                8000-16000 元/月
            </li>
            <li class="job-address">
                上海-嘉定 | 3-5年 | 本科
                                    <span title='WEB前端开发'>
                        | WEB前端开发
                    </span>
                            </li>
            <li class="job-company" title='昆山典臣信息咨询有限公司'>
                昆山典臣信息咨询有限公司
            </li>
        </ul>
        <p class="l3">
            工作职责： 1、负责企业内部系统开发和优化； 2、与需求人员和后台人员沟通，理解业务，使用合适的解决方案解决用户问题； 3、关注前端前沿技术研究，通过新技术服务团队和业务； 4、工作中主要用到的技术栈是Angular、TypeScript等。   任职要求： 1、计算机相关专业及本科学历，三年以上前端工作经验； 2、...
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>年底双薪</span>
                                                                                <span>交通补助</span>
                                                                                <span>房补</span>
                                                                                <span>饭补</span>
                                                                                <span>加班补助</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/kefu/40420338821281x.shtml">
        <ul class="l1">
            <li class="job-name" title="回访客服/双休" data-info="40420338821281">
                回访客服/双休
            </li>
            <li class="fabu-date">
                2020-08-02
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                7000-12000 元/月
            </li>
            <li class="job-address">
                上海-浦东-陆家嘴 | 经验不限 | 学历不限
                                    <span title=''>
                        | 
                    </span>
                            </li>
            <li class="job-company" title='上海盛赞企业管理有限公司'>
                上海盛赞企业管理有限公司
            </li>
        </ul>
        <p class="l3">
            信用卡前端提醒 1、按照信用卡初级的催收策略（严格按照培训资料催收话术实施），对初级风险的账户利用电话、短信等手段进行催收； 2、将工作中遇到的各种问题及时向组长汇报，对于特殊案例应交由组长处理； 3、对逾期账户的情况进行专业管理，根据客户实际要求做相应业务处理，及时反馈问题，向专业公司发起协办请求，配合其他催收方式的开展。教育程度： 全日制大学专科及以上学历<br...
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>包吃</span>
                                                                                <span>周末双休</span>
                                                                                <span>房补</span>
                                                                                <span>话补</span>
                                                                                <span>饭补</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/tech/43593673374628x.shtml">
        <ul class="l1">
            <li class="job-name" title="前端工程师" data-info="43593673374628">
                前端工程师
            </li>
            <li class="fabu-date">
                2020-09-20
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                3500-7000 元/月
            </li>
            <li class="job-address">
                上海-浦东-航头  | 经验不限 | 学历不限
                                    <span title='WEB前端开发'>
                        | WEB前端开发
                    </span>
                            </li>
            <li class="job-company" title='上海万桥信息科技有限公司'>
                上海万桥信息科技有限公司
            </li>
        </ul>
        <p class="l3">
            1.能够利用HTML+CSS实现结构搭建合理、兼容性好、扩展性强、有利于前后台的数据交互的前端网页。 2. 能够利用原生JavaScript实现复杂的前端网页交互效果，能够运用JavaScript高级知识优化代码性能。 3. 在实际项目开发中，能够运用各种各样的前端框架进行快速开发，比如animate.css、Vue.js、jQuery.js等，要求前端开发工程师需具备一定的...
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>交通补助</span>
                                                                                <span>饭补</span>
                                                                                <span>五险一金</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/tech/43542350174734x.shtml">
        <ul class="l1">
            <li class="job-name" title="前端工程师" data-info="43542350174734">
                前端工程师
            </li>
            <li class="fabu-date">
                2020-09-15
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                8000-10000 元/月
            </li>
            <li class="job-address">
                上海-浦东-张江 | 经验不限 | 学历不限
                                    <span title='WEB前端开发'>
                        | WEB前端开发
                    </span>
                            </li>
            <li class="job-company" title='上海济士智能科技有限公司'>
                上海济士智能科技有限公司
            </li>
        </ul>
        <p class="l3">
            工作内容：前端页面设计和开发 职位要求：熟悉VUE框架， javascript html 工作时间：
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>周末双休</span>
                                                                                <span>五险一金</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/tech/44269093316232x.shtml">
        <ul class="l1">
            <li class="job-name" title="前端工程师" data-info="44269093316232">
                前端工程师
            </li>
            <li class="fabu-date">
                2020-11-20
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                薪资面议 
            </li>
            <li class="job-address">
                上海-浦东-唐镇 | 3-5年 | 本科
                                    <span title='WEB前端开发'>
                        | WEB前端开发
                    </span>
                            </li>
            <li class="job-company" title='上海新微芑宣物联网有限公司'>
                上海新微芑宣物联网有限公司
            </li>
        </ul>
        <p class="l3">
            1、熟练掌握react前端框架，熟悉Ant-Design组件库及DVA 2、精通HTML5、JavaScript、CSS技术，熟练掌握HTML中各元素及其属性，并能合理运用；  3、熟悉各主流移动浏览器（IE6/7/8/9/10、360、遨游、Google Chrome、FireFox、Safari）之间的差异性，能快速定位、解决开发中遇到的浏览器兼容性问题； 4、熟悉常用的Web前端优化方法
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>免费培训</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/tech/43937494532888x.shtml">
        <ul class="l1">
            <li class="job-name" title="web前端（可兼职）" data-info="43937494532888">
                web前端（可兼职）
            </li>
            <li class="fabu-date">
                2020-11-28
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                薪资面议 
            </li>
            <li class="job-address">
                上海-嘉定-江桥 | 3-5年 | 大专
                                    <span title='WEB前端开发'>
                        | WEB前端开发
                    </span>
                            </li>
            <li class="job-company" title='上海忻怡网络科技有限公司'>
                上海忻怡网络科技有限公司
            </li>
        </ul>
        <p class="l3">
            工作内容： 职位要求：网站网页制作，编辑排版 1、熟练掌握PHP软件开发、MySQL 数据库使用; 2、熟练掌握MVC架构、ThinkPHP框架结构; 3、熟练掌握CSS、JS、jQuery、bootstrap等 网页设计； 工作时间：朝九晚六，做六休一
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>做六休一</span>
                                                                                <span>朝九晚六</span>
                                                                                <span>五险一金</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/tech/42951680641447x.shtml">
        <ul class="l1">
            <li class="job-name" title="前端工程师" data-info="42951680641447">
                前端工程师
            </li>
            <li class="fabu-date">
                2020-07-24
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                薪资面议 
            </li>
            <li class="job-address">
                上海-杨浦-五角场 | 经验不限 | 本科
                                    <span title='WEB前端开发'>
                        | WEB前端开发
                    </span>
                            </li>
            <li class="job-company" title='上海奇甲信息科技有限公司'>
                上海奇甲信息科技有限公司
            </li>
        </ul>
        <p class="l3">
            1. 负责基于 Node.js 的应用开发，打造适合网络安全各业务场景的企业级应用框架； 2. 熟练使用 ElasticSearch、 MongoDB及MySQL等关系型非关系型数据库； 3. 负责 各类网络安全解决方案的Web 前端研发；
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>急招</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/tech/42567547273481x.shtml">
        <ul class="l1">
            <li class="job-name" title="前端工程师" data-info="42567547273481">
                前端工程师
            </li>
            <li class="fabu-date">
                2020-09-24
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                5000-8000 元/月
            </li>
            <li class="job-address">
                上海-普陀 | 经验不限 | 本科
                                    <span title='WEB前端开发'>
                        | WEB前端开发
                    </span>
                            </li>
            <li class="job-company" title='上海朗通科技有限公司'>
                上海朗通科技有限公司
            </li>
        </ul>
        <p class="l3">
            岗位职责： 1、利用HTML5相关技术开发移动平台的web前端页面效果实现； 2、根据产品设计实现页面交互，与后台工程师共同实现产品功能，完成数据交互、动态信息展现； 3、协助设计师实现页面及交互，协助产品完善需求，提供技术实现方案； 4、优化代码及实现技术，提高页面性能； 5、需有layui项目工作经验。 任职要求： 1、有...
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>周末双休</span>
                                                                                <span>年底双薪</span>
                                                                                <span>五险一金</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/tech/43626266641063x.shtml">
        <ul class="l1">
            <li class="job-name" title="前端开发工程师" data-info="43626266641063">
                前端开发工程师
            </li>
            <li class="fabu-date">
                2020-10-09
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                10000-15000 元/月
            </li>
            <li class="job-address">
                上海-闵行-虹桥 | 1-2年 | 大专
                                    <span title='软件工程师'>
                        | 软件工程师
                    </span>
                            </li>
            <li class="job-company" title='上海远洲核信软件科技股份有限公司'>
                上海远洲核信软件科技股份有限公司
            </li>
        </ul>
        <p class="l3">
            工作职责： 1、业务模块前端代码开发； 2、配合后端工程师进行应用系统整合及开发； 3、持续优化前端代码，提高前端的用户体验； 4、协助完成项目的测试、系统交付工作，对项目实施提供支持。 任职要求： 1、专科及以上学历，2年以上前端开发工作经验，能独立完成前端任务开发； 2、精通Javascript、CSS、HTML、DOM等...
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>周末双休</span>
                                                                                <span>五险一金</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/tech/44015252378896x.shtml">
        <ul class="l1">
            <li class="job-name" title="前端开发工程师" data-info="44015252378896">
                前端开发工程师
            </li>
            <li class="fabu-date">
                2020-11-24
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                15000-30000 元/月
            </li>
            <li class="job-address">
                上海-闵行-江川路 | 3-5年 | 本科
                                    <span title='WEB前端开发'>
                        | WEB前端开发
                    </span>
                            </li>
            <li class="job-company" title='成都梁臻信息科技有限公司'>
                成都梁臻信息科技有限公司
            </li>
        </ul>
        <p class="l3">
            职位要求： 1、一本以上，计算机相关专业； 2、有3年以上前端项目开发经验(有完整项目开发案例最好) 3、有小程序研发经验，熟悉使用前端框架vuejs或者angularjs等, API吸组件,精通JS 4、熟悉html5,css3 5、了解现在流行前端框架vuejs等 6、熟练使用javascript, HTML, CSS等语言;<br...
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>饭补</span>
                                                                                <span>年底双薪</span>
                                                                                <span>周末双休</span>
                                                                                <span>五险一金</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/tech/42988644281496x.shtml">
        <ul class="l1">
            <li class="job-name" title="前端开发经理助理" data-info="42988644281496">
                前端开发经理助理
            </li>
            <li class="fabu-date">
                2020-08-11
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                薪资面议 
            </li>
            <li class="job-address">
                上海-长宁-仙霞 | 3-5年 | 本科
                                    <span title='WEB前端开发'>
                        | WEB前端开发
                    </span>
                            </li>
            <li class="job-company" title='上海楚赞网络科技有限公司'>
                上海楚赞网络科技有限公司
            </li>
        </ul>
        <p class="l3">
            要求：1. 211/985学历，1-7年经验。2.必须有移动端前端开发经验。3.男女不限。4.技术栈：VUE。5.33以内 位职责： 1、根据设计需求，完成页面交互效果开发； 2、据项目需要安排自己的开发计划，并按计划按质量交付所分配工作； 3、配合产品、测试完成项目开发迭代，解决问题，优化和提升用户体验； 4、完成上级交代的其他工作。 岗位要求: 1、本科及以上学历，计算机相关专业优先，具有前...
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>急招</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/tech/42935604106764x.shtml">
        <ul class="l1">
            <li class="job-name" title="前端开发工程师" data-info="42935604106764">
                前端开发工程师
            </li>
            <li class="fabu-date">
                2020-10-29
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                12000-20000 元/月
            </li>
            <li class="job-address">
                上海-普陀-长风 | 3-5年 | 大专
                                    <span title='WEB前端开发'>
                        | WEB前端开发
                    </span>
                            </li>
            <li class="job-company" title='酷宝信息技术（上海）有限公司'>
                酷宝信息技术（上海）有限公司
            </li>
        </ul>
        <p class="l3">
            关于我们： www.5173.com（中国网络游戏服务网）是中国成立最早（2003年），规模最大的专业游戏交易平台，用户超过一亿，涵盖了500多家游戏运营商。在东京、新加坡、香港、上海、浙江员工600余人。中国互联网百强企业、中国电子商务百强企业、浙江省高新技术百强企业。多次获得“最佳雇主”称号，我们的目标是客户满意度120%，员工满意度120%。目前正在拓展日本、美国、台湾、韩国等全...
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>饭补</span>
                                                                                <span>交通补助</span>
                                                                                <span>周末双休</span>
                                                                                <span>五险一金</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/kefu/44079904942487x.shtml">
        <ul class="l1">
            <li class="job-name" title="贷款前端审核客服岗" data-info="44079904942487">
                贷款前端审核客服岗
            </li>
            <li class="fabu-date">
                2020-11-11
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                6000-8000 元/月
            </li>
            <li class="job-address">
                上海-浦东 | 经验不限 | 大专
                                    <span title='客服专员/助理'>
                        | 客服专员/助理
                    </span>
                            </li>
            <li class="job-company" title='中国平安财产保险股份有限公司浙江分公司'>
                中国平安财产保险股份有限公司浙江分公司
            </li>
        </ul>
        <p class="l3">
            工作内容 银行每天提供有贷款意向名单数量在100--150条，做问卷调查，大概10几个问题，筛选出优质客户资料流转至销售，销售做进一步产品销售工作，工作内容相对简单，无压力。 薪资待遇： 1、签订正式劳动合同 缴纳国家规定五险一金 2、底薪2800+津贴补助+筛远名单数量绩效平均薪资6千到8千左右、（每季度考核一次，考核通过晋升一级加300元工资，共12个...
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>交通补助</span>
                                                                                <span>五险一金</span>
                                                                                <span>房补</span>
                                                                                <span>加班补助</span>
                                                                                <span>周末双休</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/tech/41304971849122x.shtml">
        <ul class="l1">
            <li class="job-name" title="前端开发工程师" data-info="41304971849122">
                前端开发工程师
            </li>
            <li class="fabu-date">
                2020-11-27
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                12000-15000 元/月
            </li>
            <li class="job-address">
                上海-闵行-梅陇 | 1-2年 | 本科
                                    <span title='WEB前端开发'>
                        | WEB前端开发
                    </span>
                            </li>
            <li class="job-company" title='上海崇法数据科技有限公司'>
                上海崇法数据科技有限公司
            </li>
        </ul>
        <p class="l3">
            职位要求：2年以上开发经验，精通Java,JS,有App，小程序开发能力；熟悉C#,.net优先；有政府类项目开发维护经验优先。
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>周末双休</span>
                                                                                <span>五险一金</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/yewu/42257456458274x.shtml">
        <ul class="l1">
            <li class="job-name" title="电话客服/前端电话销售" data-info="42257456458274">
                电话客服/前端电话销售
            </li>
            <li class="fabu-date">
                2020-07-27
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                5000-10000 元/月
            </li>
            <li class="job-address">
                上海-浦东-川沙 | 经验不限 | 学历不限
                                    <span title='电话销售'>
                        | 电话销售
                    </span>
                            </li>
            <li class="job-company" title='上海毓昶商务咨询有限公司'>
                上海毓昶商务咨询有限公司
            </li>
        </ul>
        <p class="l3">
            工作内容： 1、通过推广数据，进行电话，全程只需要跟客户电话沟通，进行前端客服！ 2、根据公司要求就是拨打电话，只做前端呼出，就是电话客服！ 职位要求： 1、18-28岁，高中和大专及以上学历！！ 2、乐观、自信、有责任感，愿意挑战高薪，有较强抗压能力；有经验者勿扰！ 工作时间： 1：无经验者可提供专业带薪培训，公司提供优质资...
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>每周团建</span>
                                                                                <span>加班补助</span>
                                                                                <span>饭补</span>
                                                                                <span>交通补助</span>
                                                                                <span>话补</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/tech/43648759607937x.shtml">
        <ul class="l1">
            <li class="job-name" title="web前端工程师" data-info="43648759607937">
                web前端工程师
            </li>
            <li class="fabu-date">
                2020-09-25
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                薪资面议 
            </li>
            <li class="job-address">
                上海-虹口-江湾 | 3-5年 | 本科
                                    <span title='WEB前端开发'>
                        | WEB前端开发
                    </span>
                            </li>
            <li class="job-company" title='上海远哲电子技术有限公司'>
                上海远哲电子技术有限公司
            </li>
        </ul>
        <p class="l3">
            工作内容：负责web的前端开发工作；能够主动与UI设计师、后台开发工程师协作；能关注web的前沿技术并不断学习 职位要求： 1、一至三年以上Web前端开发经验 2、精通Javascript，熟练手写原生JS代码，精通各种前端调试工具； 熟悉JS性能优化；能使用如Jquery,Bootstrap等各种前端技术和框架！ 3、熟练运用CSS3新特性，熟悉HTML...
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>饭补</span>
                                                                                <span>加班补助</span>
                                                                                <span>年底双薪</span>
                                                                                <span>周末双休</span>
                                                                                <span>五险一金</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/tech/44203615990542x.shtml">
        <ul class="l1">
            <li class="job-name" title="WEB前端开发工程师" data-info="44203615990542">
                WEB前端开发工程师
            </li>
            <li class="fabu-date">
                2020-11-14
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                薪资面议 
            </li>
            <li class="job-address">
                上海-浦东-三林 | 3-5年 | 本科
                                    <span title='WEB前端开发'>
                        | WEB前端开发
                    </span>
                            </li>
            <li class="job-company" title='上海驾哿企业管理中心'>
                上海驾哿企业管理中心
            </li>
        </ul>
        <p class="l3">
            完成Web前端应用、交互代码开发
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>急招</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/tech/42774518509204x.shtml">
        <ul class="l1">
            <li class="job-name" title="WEB前端开发工程师" data-info="42774518509204">
                WEB前端开发工程师
            </li>
            <li class="fabu-date">
                2020-07-14
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                薪资面议 
            </li>
            <li class="job-address">
                上海-青浦-华新 | 3-5年 | 大专
                                    <span title='WEB前端开发'>
                        | WEB前端开发
                    </span>
                            </li>
            <li class="job-company" title='火神（上海）网络科技有限公司'>
                火神（上海）网络科技有限公司
            </li>
        </ul>
        <p class="l3">
            完成Web前端应用、交互代码开发
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>饭补</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/tech/43813535842341x.shtml">
        <ul class="l1">
            <li class="job-name" title="WEB前端开发工程师" data-info="43813535842341">
                WEB前端开发工程师
            </li>
            <li class="fabu-date">
                2020-10-10
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                12000-19000 元/月
            </li>
            <li class="job-address">
                上海-闵行-梅陇 | 经验不限 | 本科
                                    <span title='WEB前端开发'>
                        | WEB前端开发
                    </span>
                            </li>
            <li class="job-company" title='合肥爱休信息科技有限公司'>
                合肥爱休信息科技有限公司
            </li>
        </ul>
        <p class="l3">
            职位描述： 1、依据产品需求完成高质量的跨终端Web Mobile/Node.js的前端开发和维护 2、对具体的产品进行 性能优化，实现极致的页面加载、执行和渲染时间 3、在理解前端开发流程的基础上，结合前端实际建立或优化提升工作效率的工具 4、在理解产品业务的基础上，提升产品的用户体验，技术驱动业务的发展 5、关注前端前沿技术研究，通过新技术服...
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>年底双薪</span>
                                                                                <span>周末双休</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/tech/44093554336786x.shtml">
        <ul class="l1">
            <li class="job-name" title="前端开发15-20k" data-info="44093554336786">
                前端开发15-20k
            </li>
            <li class="fabu-date">
                2020-11-09
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                15000-25000 元/月
            </li>
            <li class="job-address">
                上海-静安 | 3-5年 | 本科
                                    <span title='WEB前端开发'>
                        | WEB前端开发
                    </span>
                            </li>
            <li class="job-company" title='上海伽利服装有限公司'>
                上海伽利服装有限公司
            </li>
        </ul>
        <p class="l3">
            岗位职责 1.前端框架的设计与实现，各业务模块前端代码开发； 2.使用技术例如HTML5/CSS/Vue，来实现我们的产品前端。 3. 与后端开发人员配合，完成开发工作 任职要求 1、2年以上前端开发经验; 2、熟练掌握Vue技术栈; 3、熟练使用HTML5、CSS3、Jquery、Javascript、ES5/6、TS等前端...
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>节假日三薪</span>
                                                                                <span>带薪年假</span>
                                                                                <span>房补</span>
                                                                                <span>饭补</span>
                                                                                <span>年底双薪</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
        
    <div class="jobList pc_search_listclick" data-detail="http://www.chinahr.com/detail/sh/tech/43806174034953x.shtml">
        <ul class="l1">
            <li class="job-name" title="前端小程序开发程序师" data-info="43806174034953">
                前端小程序开发程序师
            </li>
            <li class="fabu-date">
                2020-11-05
                                <input type="hidden" name="sourceType" value="1" collectState="false">
                            </li>
        </ul>
        <ul class="l2">
            <li class="job-salary">
                13000-16000 元/月
            </li>
            <li class="job-address">
                上海-浦东-御桥 | 3-5年 | 本科
                                    <span title='WEB前端开发'>
                        | WEB前端开发
                    </span>
                            </li>
            <li class="job-company" title='上海佳贝教育信息咨询有限公司'>
                上海佳贝教育信息咨询有限公司
            </li>
        </ul>
        <p class="l3">
            前端：小程序前端开发工程师  岗位职责： 负责公司微信小程序和web前端的开发，维护和优化工作。 参与项目计划和需求的讨论，从技术角度提供建议。配合产品经理设计界面原型。 负责页面相关接入层开发，与后端工程师配合对接，共同协作完成项目。  岗位要求： 专科以上学历，3年以上前端相关工作经验，能依照设计稿，独立设计并高质量的完成项目。 精通微信小程序开发，能独立完成微信小程序前端从0到1的建设。精...
        </p>
        <ul class="l4">
            <li class="job-fuli">
                                <div class="job_wel clearfix">
                                                            <span>环境好</span>
                                                                                <span>周末双休</span>
                                                                                <span>免费培训</span>
                                                        </div>
                            </li>
            <li class="job-shenqing">
                <div class="pc_search_coll_tip">可在个人中心查看</div>
                <div class="pc_search_coll">
                    收藏
                </div>
                <a href="javascript:void(0)" class="pc_search_deliver">
                    查看职位
                </a>
            </li>
        </ul>

    </div>
    </div>

            <!-- 异步广告位 -->
            <div id="advertisement"></div>
            <!--海外运营广告位-->
            <div id="search_advertisement"></div>
            <!-- 清除浮动 -->
            <div class="clearfix"></div>

            <!-- 总页数 -->
            <input type="hidden" class="total-page" value="70" />
            <!-- 分页 -->
                        <div class="page-list">
                 <a class="page-prev" herf="javascript:void(0)"><i class="prevBtn iconfont"></i></a><a class="page-item active" herf="javascript:void(0)">1</a><a class="page-item" href="http://search.chinahr.com/sh/job/pn2/?key=%E5%89%8D%E7%AB%AF">2</a><a class="page-item" href="http://search.chinahr.com/sh/job/pn3/?key=%E5%89%8D%E7%AB%AF">3</a><a class="page-item" href="http://search.chinahr.com/sh/job/pn4/?key=%E5%89%8D%E7%AB%AF">4</a><a class="page-item" href="http://search.chinahr.com/sh/job/pn5/?key=%E5%89%8D%E7%AB%AF">5</a><a class="page-item" href="http://search.chinahr.com/sh/job/pn6/?key=%E5%89%8D%E7%AB%AF">6</a><a class="page-item" href="http://search.chinahr.com/sh/job/pn7/?key=%E5%89%8D%E7%AB%AF">7</a><a class="page-item" href="http://search.chinahr.com/sh/job/pn8/?key=%E5%89%8D%E7%AB%AF">8</a><a class="page-next" href="http://search.chinahr.com/sh/job/pn2/?key=%E5%89%8D%E7%AB%AF"><i class="nextBtn iconfont"></i></a>
            </div>
            
            <!-- 反馈 -->
            <div class="fankui-and-top">
    <div id="toTop">
    </div>
    <div id="fankui">
    </div>
</div>        </div>
    </div>
</div>

<!-- FooterBar -->
<div id="commonFoot"></div>
<script type="text/javascript" src="//j1.58cdn.com.cn/git/hrg-fe-zhaopin-chinahr/chinahr-common-source-pc/jquery-1.11.3.min_v20190909201414.js">
</script>
<script src="//tracklog.58.com/referrer4.js"></script>
<script type="text/javascript" src="//j1.58cdn.com.cn/componentsLoader/dist/ComponentsLoader_v20201214135219.js"></script>
<script type="text/javascript" src="//j1.58cdn.com.cn/job/pc/chinahr/common/0.2/commonBar_v20201123150147.js">
</script>
<script type="text/javascript" src="//j1.58cdn.com.cn/git/hrg-fe-zhaopin-chinahr/chinahr-list-pc/static/js/slef-control_v20201123150458.js">
</script>
<script type="text/javascript" src="//j1.58cdn.com.cn/job/pc/chinahr/searchlist/0.1/js/feedback_v20180904095221.js">
</script>
<script type="text/javascript" src="//j1.58cdn.com.cn/git/hrg-fe-zhaopin-chinahr/chinahr-list-pc/static/js/main_v20201123150458.js">
</script>
</body>

</html>
'''
import json,re
response=etree.HTML(a)
json_data=re.findall('____json4fe = .*?({"dispid":".*?","name":".*?","listname":".*?"}).*?;',a,re.S)[0]
city=json.loads(json_data).get('name')
print(city)
# job_list=response.xpath('//div[@class="jobList pc_search_listclick"]/@data-detail')
# next_page = response.xpath('//*[@class="page-next"]/@href')
# print(next_page)
