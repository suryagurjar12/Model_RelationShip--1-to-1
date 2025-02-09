# Generated by Django 5.0.7 on 2024-07-17 12:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adhar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adhar_no', models.IntegerField(unique=True)),
                ('create_date', models.DateTimeField()),
                ('create_by', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('adhar_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.adhar')),
            ],
        ),
    ]
