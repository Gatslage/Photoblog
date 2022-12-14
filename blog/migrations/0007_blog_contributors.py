# Generated by Django 3.2.5 on 2022-09-12 22:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_remove_blog_contributors'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='contributors',
            field=models.ManyToManyField(related_name='contributions', through='blog.interBlogUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
