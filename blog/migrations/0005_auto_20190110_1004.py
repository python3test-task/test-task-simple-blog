# Generated by Django 2.1.5 on 2019-01-10 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190110_1000'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follower',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='follower',
            name='follower',
        ),
        migrations.RemoveField(
            model_name='follower',
            name='following',
        ),
        migrations.DeleteModel(
            name='Follower',
        ),
    ]
