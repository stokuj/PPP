# Generated by Django 4.1.3 on 2023-01-03 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_remove_profile_selectmenu'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='selectMenu',
            field=models.BooleanField(default=False),
        ),
    ]
