# Generated by Django 3.1.1 on 2020-09-19 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0003_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_seen',
            field=models.DateTimeField(blank=True, default=None),
        ),
    ]
