from django.db import models
from stdimage import StdImageField
from django.conf import settings
# Create your models here.


class UploadFile(models.Model):
    file = StdImageField(
        upload_to='pictures/', variations={
            'large': (600, 400),
            'thumbnail': (100, 100, True),
            'medium': (300, 200),
        })

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.url
