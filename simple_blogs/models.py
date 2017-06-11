from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Theme(models.Model):
    """博客主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class Content(models.Model):
    """主题内容"""
    theme = models.ForeignKey(Theme)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'contents'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50] + "..."
