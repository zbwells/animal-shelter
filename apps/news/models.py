## Amber Shackleford.
## Part of the Wise Animal Shelter Management System Project.
##
## Released under the terms of the MIT License.
## See LICENSE for details.

from django.db import models

# Create your models here.

from django.db import models


class Post(models.Model):
	post_text = models.TextField(max_length=10000)
	pub_date = models.DateTimeField("date published")
	image = models.FileField(upload_to="uploads/%Y/%m/", default="", blank=True,null=True)
	def __str__(self):
		return self.post_text
	def recent(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

