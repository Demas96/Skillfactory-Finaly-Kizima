# Generated by Django 4.0.5 on 2022-06-16 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0007_alter_usercode_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercode',
            name='code2',
        ),
    ]
