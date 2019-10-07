from django.db import models
from django.utils import timezone

# Create your models here.


class Comment(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    article_id = models.IntegerField()
    blog_id = models.IntegerField(default=0)
    created_date = models.DateField(default=timezone.now)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.author
