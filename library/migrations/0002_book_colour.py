# Generated by Django 4.0.1 on 2022-01-08 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='colour',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]