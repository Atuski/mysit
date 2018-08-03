from django.conf.urls import url
from .views import *
urlpatterns = [
	url(r'^$',blog_list,name='blog_list'),#	博客的首页，展示博文列表
	url(r'^(\d+)$',blog_detail,name='blog_details'),#博文页详情
	url(r'^blogtype/(\d+)$',blog_type,name='blogtype'),#博文分类展示
	url(r'^date/(19|20\d{2})/([1-9]|1[0-2])',blog_date,name='blogdate')#博文的按月统计
]
