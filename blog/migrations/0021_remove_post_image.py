# Generated by Django 2.2.5 on 2019-11-05 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20191018_0932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
