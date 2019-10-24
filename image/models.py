from django.db import models

# Create your models here.


class UploadFile(models.Model):
    file = models.ImageField(
        upload_to='pictures/', null=True, blank=True)

    def __str__(self):
        return self.file.url
