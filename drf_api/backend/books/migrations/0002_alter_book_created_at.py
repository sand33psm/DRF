# Generated by Django 4.2.16 on 2024-09-20 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
