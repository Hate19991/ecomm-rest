# Generated by Django 5.1.2 on 2024-11-03 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
