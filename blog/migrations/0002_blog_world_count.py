# Generated by Django 3.2.5 on 2022-09-10 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='world_count',
            field=models.IntegerField(null=True),
        ),
    ]
