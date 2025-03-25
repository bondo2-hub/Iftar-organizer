# Generated by Django 5.1.3 on 2025-03-25 11:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='host',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sent_notifications', to=settings.AUTH_USER_MODEL),
        ),
    ]
