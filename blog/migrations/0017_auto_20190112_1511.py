# Generated by Django 2.1.5 on 2019-01-12 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20190112_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='read',
            name='reader',
        ),
        migrations.RemoveField(
            model_name='read',
            name='readers',
        ),
        migrations.DeleteModel(
            name='Read',
        ),
    ]