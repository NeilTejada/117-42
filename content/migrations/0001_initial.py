# Generated by Django 5.0.2 on 2024-03-01 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('descrtiption', models.TextField()),
                ('year', models.IntegerField()),
                ('image', models.ImageField(upload_to='static/img/')),
                ('repository', models.URLField()),
                ('skill', models.ManyToManyField(to='content.skill')),
            ],
        ),
    ]
