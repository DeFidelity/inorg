# Generated by Django 3.2.6 on 2021-08-25 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0011_alter_notification_from_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/post_photo'),
        ),
    ]
