# Generated by Django 3.1.5 on 2021-03-01 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangopage', '0002_auto_20210301_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdfupload',
            name='fileUpload',
            field=models.FileField(blank=True, upload_to='media/'),
        ),
    ]
