# Generated by Django 5.1.4 on 2025-01-12 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='points',
        ),
    ]
