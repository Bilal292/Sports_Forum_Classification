# Generated by Django 3.2.1 on 2021-05-05 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_post_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='testCategories', max_length=100),
        ),
    ]
