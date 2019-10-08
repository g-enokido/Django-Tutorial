from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='タイトル')
    text = models.TextField(verbose_name='投稿内容')
    created_date = models.DateTimeField(default=timezone.now)
    blog_id = models.IntegerField()
    category_id = models.IntegerField(default=0)
    image = models.ImageField(
        upload_to='pictures/', null=True, blank=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.title)


class Category(models.Model):
    holder = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=200, verbose_name='カテゴリー名')
    blog_id = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField()
