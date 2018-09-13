from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.fields import exceptions
from django.contrib.contenttypes.models import ContentType
from read_statistics.models import *
# Create your models here.
class BlogType(models.Model):
	type_name = models.CharField(max_length=30)
	def __str__(self): 
		return self.type_name
	class Meta:
		verbose_name_plural=verbose_name='分类'
class Blog(models.Model):
	title = models.CharField(max_length=30,verbose_name="主题")
	content = RichTextUploadingField(verbose_name="内容")
	author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
	created_time = models.DateTimeField(auto_now_add=True)
	last_updatetime = models.DateTimeField(auto_now=True)
	blog_type = models.ForeignKey(BlogType,on_delete=models.DO_NOTHING)
	#read_num = models.IntegerField(default = 0)
	def get_read_num(self):
		try:
			ct = ContentType.objects.get_for_model(Blog)
			readnum = ReadNum.objects.get(content_type=ct,object_id=self.pk)
			return readnum.read_num
		except exceptions.ObjectDoesNotExist:
			return 0
	def __str__(self):
		return "title:%s"%self.title
	class Meta:
		verbose_name = '博客'
		verbose_name_plural = verbose_name
		ordering = ['-created_time']
		'''
class ReadNum(models.Model):
	read_num = models.IntegerField(default=0)
	blog = models.OneToOneField(Blog,on_delete=models.DO_NOTHING)
'''