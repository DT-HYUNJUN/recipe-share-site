# Generated by Django 3.2.18 on 2023-05-29 06:19

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_recipe_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
