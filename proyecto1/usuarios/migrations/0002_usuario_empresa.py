# Generated by Django 5.0 on 2023-12-24 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='empresa',
            field=models.CharField(default='empresa', max_length=50),
        ),
    ]
