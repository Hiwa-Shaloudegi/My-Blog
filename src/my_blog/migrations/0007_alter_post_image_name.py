# Generated by Django 3.2.8 on 2022-01-09 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0006_post_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_name',
            field=models.CharField(default='my_blog/images/default.png', max_length=64, null=True),
        ),
    ]
