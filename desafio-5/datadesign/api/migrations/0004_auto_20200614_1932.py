# Generated by Django 3.0.6 on 2020-06-14 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200614_1901'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='agent_id',
            new_name='agent',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='groupuser',
            old_name='group_id',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='groupuser',
            old_name='user_id',
            new_name='user',
        ),
    ]
