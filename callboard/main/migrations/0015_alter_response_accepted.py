# Generated by Django 4.0.5 on 2022-06-17 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_advertisement_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='accepted',
            field=models.BooleanField(default=False, verbose_name='Принято'),
        ),
    ]
