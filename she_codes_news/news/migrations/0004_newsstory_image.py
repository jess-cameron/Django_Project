# Generated by Django 4.2.2 on 2023-07-22 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_userfavorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news.images/'),
        ),
    ]
