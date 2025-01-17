# Generated by Django 5.0.3 on 2024-03-31 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=80)),
                ('user_name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=60)),
                ('number', models.IntegerField(default=18)),
                ('password', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=20)),
            ],
        ),
    ]
