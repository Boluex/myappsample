# Generated by Django 3.2.9 on 2022-02-10 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_auto_20220210_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='tagline',
            field=models.CharField(max_length=20000),
        ),
    ]