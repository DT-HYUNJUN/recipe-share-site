# Generated by Django 3.2.18 on 2023-06-13 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
