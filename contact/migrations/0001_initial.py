# Generated by Django 3.2.9 on 2021-12-03 06:18

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email_address', models.EmailField(max_length=254)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('subject', models.TextField(max_length=500)),
            ],
        ),
    ]
