# Generated by Django 3.2.18 on 2023-05-30 08:41

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_liked_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='color',
            field=colorfield.fields.ColorField(blank=True, default='', image_field='image', max_length=18, samples=None),
        ),
    ]