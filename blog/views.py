from django.shortcuts import render,get_object_or_404,render_to_response
from .models import * 
from django.core.paginator import Paginator
# Create your views here.
#展示博客列表和部分内容信息
def blog_list(request):
	blogs = Blog.objects.all()
	# blogtypes = blogs.author.objects.all()
	blogtypes = BlogType.objects.all()
	page_list_all = Paginator(blogs,3)
	#获取页面url的参数，也就是具体页数，如果没有get到值的话，默认开始为第一页
	page_num = request.GET.get('page',1)
	#获得某一页的page的对象
	page_of_blogs = page_list_all.page(page_num)
	#获取博文的发表时间年月列表
	blog_dates = Blog.objects.dates('created_time','month',order='DESC')
	return render(request,'blog/blog_list.html',locals())
#展示博客内容页面
def blog_detail(request,blog_id):
	blog = Blog.objects.get(id=blog_id)
	current_time = blog.created_time
	context = {}
	context['blogs_obj']=blog
	#筛选出大于当前文章时间的文章，由于排序按照时间从大到小，利用last函数选择最后一个列表元素
	previous_blog = Blog.objects.filter(created_time__gt=current_time).last()
	#利用first函数选择第一个元素，也就是下一篇博客，也可使用.[0]选出列表第一个元素
	next_blog = Blog.objects.filter(created_time__lt=current_time).first()
	context['next_blog']=next_blog
	context['previous_blog']=previous_blog
	#计数功能
	if not request.COOKIES.get('blog_%s_read' % blog.pk):
		blog.read_num += 1
	blog.save()
	context['read_num'] = blog.read_num
	#设置cookie
	response = render(request,'blog/blog_detail.html',context)
	response.set_cookie('blog_%s_read' % blog.pk,'true')
	return response
#按照分类展示博客
def blog_type(request,blogtype_id):
	context = {}
	#筛选出id=blogtype_id的BlogType
	blogtype = get_object_or_404(BlogType,pk=blogtype_id)
	context['blogtype'] = blogtype
	#筛选出和BlogType 对应的博客有哪些
	blogs = Blog.objects.filter(blog_type=blogtype)
	context['blogs']=blogs
	return render_to_response('blog/blog_type.html',context)
#按照发布时间展示博客
def blog_date(request,year,month):
	#获取博客时间符合要求的博文
	blogs = Blog.objects.filter(created_time__year=year,created_time__month=month)
	return render(request,'blog/blog_date.html',locals())
