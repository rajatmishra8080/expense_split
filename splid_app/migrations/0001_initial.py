# Generated by Django 4.2.3 on 2023-11-08 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]
