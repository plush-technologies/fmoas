# Generated by Django 4.2.2 on 2023-06-28 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CompleteTask',
            new_name='CompletedTask',
        ),
    ]
