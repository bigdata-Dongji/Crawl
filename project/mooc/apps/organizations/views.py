from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render_to_response

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from apps.organizations.models import CourseOrg,City
class OrgView(View):
    def get(self,request):
        all_orgs=CourseOrg.objects.all()
        org_nums=CourseOrg.objects.count()
        all_citys=City.objects.all()
        # 对课程机构数据进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs, per_page=5,request=request)
        orgs = p.page(page)


        return render(request,'org-list.html',{
            'all_orgs':orgs,
            'org_nums':org_nums,
            'all_citys':all_citys
        })

