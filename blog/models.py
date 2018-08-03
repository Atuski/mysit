from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BlogType(models.Model):
	type_name = models.CharField(max_length=30)
	def __str__(self):
		return self.type_name
	class Meta:
		verbose_name_plural=verbose_name='分类'
class Blog(models.Model):
	title = models.CharField(max_length=30,verbose_name="主题")
	content = models.TextField(verbose_name="内容")
	author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
	created_time = models.DateTimeField(auto_now_add=True)
	last_updatetime = models.DateTimeField(auto_now=True)
	blog_type = models.ForeignKey(BlogType,on_delete=models.DO_NOTHING)
	def __str__(self):
		return "title:%s"%self.title
	class Meta:
		verbose_name = '博客'
		verbose_name_plural = verbose_name
		ordering = ['-created_time']