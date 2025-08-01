# Generated by Django 5.1.4 on 2024-12-21 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256, unique=True)),
                ('isTemp', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=256)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('coordinate', models.CharField(max_length=256)),
                ('participant', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=16384)),
                ('detail_title', models.CharField(max_length=256)),
                ('detail_text', models.CharField(max_length=16384)),
                ('photo_path', models.CharField(max_length=16384)),
                ('video_path', models.CharField(max_length=16384)),
            ],
        ),
    ]
