# Generated by Django 3.2.8 on 2021-11-06 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0002_auto_20211106_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
