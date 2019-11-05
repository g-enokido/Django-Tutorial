from django.conf import settings
from django.db import models
from django.utils import timezone
from accounts.models import Blog


class Category(models.Model):
    holder = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=200, verbose_name='カテゴリー名')
    blog = models.ForeignKey(Blog, verbose_name='掲載ブログ',
                             on_delete=models.CASCADE, default=0)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField()

    def __str__(self):
        return self.category_name


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='タイトル')
    text = models.TextField(verbose_name='投稿内容')
    created_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, verbose_name='掲載ブログ',
                                 on_delete=models.CASCADE, default=0)
    published_date = models.DateTimeField(blank=True, null=True)
    blog = models.ForeignKey(Blog, verbose_name='掲載ブログ',
                             on_delete=models.CASCADE, default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.title)
