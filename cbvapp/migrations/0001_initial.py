# Generated by Django 4.1 on 2023-06-07 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('principal', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
            ],
        ),
    ]
