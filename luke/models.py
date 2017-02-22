from django.db import models
from django.utils import timezone

# Create your models here.
class BlogPost(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	summary = models.TextField()
	content = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	tags = models.CharField(max_length=200, default='Blog Post')

	def get_tag_list(self):
		return sorted(self.tags.rsplit('|'))
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

	def dash_name(self):
		dash_name = str(self.title.replace(" ", "-"))
		return dash_name

class Project(models.Model):
	title = models.CharField(max_length=200)
	summary = models.TextField()
	content = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	tags = models.CharField(max_length=200, default='Project')

	def __str__(self):
		return self.title

	def dash_name(self):
		dash_name = str(self.title.replace(" ", "-"))
		return dash_name

	def get_tag_list(self):
		return sorted(self.tags.rsplit('|'))