from django.contrib import admin
from .models import Blog,BlogType
# Register your models here.
@admin.register(Blog)
class BlogsAdmin(admin.ModelAdmin):
	list_display = ('id','title','content','author','read_num','created_time','last_updatetime','blog_type')
	list_editable =('content',)
	# search_fields = ('last_updatetime',)
	# list_filter = ('title','id',)
	# fields = ('title','content','blog_type','author',)
@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
	list_display = ('id','type_name',)
