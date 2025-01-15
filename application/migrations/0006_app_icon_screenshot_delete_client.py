# Generated by Django 5.1.4 on 2025-01-13 12:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_remove_user_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='icon',
            field=models.ImageField(default='app_icons/default_icon.png', upload_to='app_icons/'),
        ),
        migrations.CreateModel(
            name='Screenshot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screenshot', models.ImageField(upload_to='screenshots/')),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.app')),
            ],
        ),
        migrations.DeleteModel(
            name='Client',
        ),
    ]