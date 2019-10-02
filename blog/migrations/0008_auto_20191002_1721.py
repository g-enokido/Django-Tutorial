# Generated by Django 2.2.5 on 2019-10-02 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20191002_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='updated_by_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='image.png', null=True, upload_to='pitures/'),
        ),
    ]
