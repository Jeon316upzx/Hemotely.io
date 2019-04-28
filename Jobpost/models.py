from django.db import models
from datetime import datetime,timedelta
from taggit.managers import TaggableManager
from django_countries.fields import CountryField

def get_deadline():
    return datetime.today() + timedelta(days = 90)
class Job(models.Model):
      postedDate = models.DateTimeField(auto_now_add = True)
      position = models.CharField(max_length = 255)
      companyName = models.CharField(max_length = 255)
      companyLogo = models.ImageField(default = 'default.jpg', blank = True)
      companyEmail = models.EmailField(max_length = 255)
      companyApplyUrl = models.URLField()
      jobResp = models.TextField()
      jobDesc = models.TextField()
      jobReq = models.TextField()
      salary = models.IntegerField(blank = True)
      tags = TaggableManager()
      location = CountryField(multiple= True,default='')
      category = models.CharField(max_length=50,default='fulltime')
      postExpire = models.DateTimeField(default = get_deadline)

      def __str__(self):
          return self.position
