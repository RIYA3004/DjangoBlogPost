# Generated by Django 3.0.5 on 2020-06-06 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
