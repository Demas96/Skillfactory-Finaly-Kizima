# Generated by Django 4.0.5 on 2022-06-16 20:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sign', '0006_alter_usercode_code2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercode',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='valid_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
