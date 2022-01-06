# Generated by Django 3.2.8 on 2022-01-05 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0003_rename_is_valid_comment_active_comment_author_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='my_blog.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]