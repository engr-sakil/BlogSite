# Generated by Django 3.1.4 on 2021-01-05 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_blogpost_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(default='', upload_to='images/blog'),
        ),
    ]
