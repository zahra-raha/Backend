# Generated by Django 3.2.18 on 2023-06-02 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_alter_post_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
