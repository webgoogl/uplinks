# Generated by Django 4.2 on 2023-06-13 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='animecards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_photo', models.FileField(default=None, max_length=400, null=True, upload_to='cardmedia/')),
                ('a_title', models.CharField(max_length=100)),
                ('a_descript', models.CharField(max_length=1000)),
                ('a_link', models.CharField(default=None, max_length=100)),
            ],
        ),
    ]
