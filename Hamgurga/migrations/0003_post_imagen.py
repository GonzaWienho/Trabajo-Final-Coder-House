# Generated by Django 4.2 on 2023-04-25 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hamgurga', '0002_post_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]
