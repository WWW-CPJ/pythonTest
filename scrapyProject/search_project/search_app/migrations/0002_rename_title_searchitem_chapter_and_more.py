# Generated by Django 5.1.6 on 2025-02-14 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='searchitem',
            old_name='title',
            new_name='chapter',
        ),
        migrations.RemoveField(
            model_name='searchitem',
            name='content',
        ),
        migrations.RemoveField(
            model_name='searchitem',
            name='created',
        ),
        migrations.AddField(
            model_name='searchitem',
            name='link',
            field=models.CharField(default='https://www.doupocangqiong.org/doupocangqiong/', max_length=500),
        ),
    ]
