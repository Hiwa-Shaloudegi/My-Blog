# Generated by Django 3.2.8 on 2022-01-11 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0008_alter_post_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
