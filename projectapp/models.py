from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Project(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='project', null=True)  # user.article으로 접근할 수 있으므로
    title = models.CharField(max_length=200, null=True)
    subtitle = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='project/', null=False)
    created_at = models.DateField(auto_now_add=True, null=True)