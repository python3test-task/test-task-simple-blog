# Generated by Django 2.1.5 on 2019-01-12 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='read',
            name='posts',
        ),
        migrations.RemoveField(
            model_name='read',
            name='reader',
        ),
        migrations.DeleteModel(
            name='Read',
        ),
    ]
