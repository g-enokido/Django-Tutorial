from django.db import models
from django.conf import settings
from django.utils import timezone


class Blog(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog_name = models.CharField(max_length=200, verbose_name='ブログタイトル')
    blog_detail = models.TextField(null=True, blank=True, verbose_name='ブログ詳細')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.blog_name
