from django.db import models
from django.utils import timezone
from blog.models import Post
from accounts.models import Blog


# Create your models here.


class Comment(models.Model):
    author = models.CharField(max_length=200, default='名無しさん')
    text = models.TextField()
    article = models.ForeignKey(Post, verbose_name='元記事',
                                on_delete=models.CASCADE, default=0)
    blog = models.ForeignKey(Blog, verbose_name='元ブログ',
                             on_delete=models.CASCADE, default=0)
    created_date = models.DateField(default=timezone.now)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.author
