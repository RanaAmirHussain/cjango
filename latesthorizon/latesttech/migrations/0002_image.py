# Generated by Django 4.0.4 on 2022-05-13 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latesttech', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='myimage')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
