# Create your models here.
from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project


# Create your views here.
class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True) # user.article으로 접근할 수 있으므로

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True) # 꼭 created_at 컬럼에 auto_now_add로 해야 자동으로 생성된 시간 저장됨.
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_articles', null=True)