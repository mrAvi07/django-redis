# Generated by Django 3.2 on 2021-10-11 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
