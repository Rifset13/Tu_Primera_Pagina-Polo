# Generated by Django 5.0 on 2023-12-24 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_atencion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('nro_cuit', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
