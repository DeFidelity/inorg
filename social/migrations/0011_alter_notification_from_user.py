# Generated by Django 3.2.6 on 2021-08-25 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0010_auto_20210823_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='from_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification_from', to=settings.AUTH_USER_MODEL),
        ),
    ]
