# Generated by Django 2.1.5 on 2019-01-11 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_read'),
    ]

    operations = [
        migrations.RenameField(
            model_name='read',
            old_name='post',
            new_name='readers',
        ),
    ]
