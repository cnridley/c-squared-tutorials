# Generated by Django 3.1.5 on 2021-03-01 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PdfUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=254, null=True)),
                ('fileUpload', models.FileField(blank=True, upload_to='')),
            ],
        ),
    ]
