# Generated by Django 4.1.3 on 2023-01-03 17:47

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_mycsv_alter_activity_activity_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycsv',
            name='file_name',
            field=models.FileField(upload_to='csvs/', validators=[main.models.validate_file_extension]),
        ),
    ]
