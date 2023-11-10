# Generated by Django 4.2.3 on 2023-11-09 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splid_app', '0002_expence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expence',
            name='expenseAmount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='expence',
            name='expenseBy',
            field=models.CharField(max_length=100),
        ),
    ]
