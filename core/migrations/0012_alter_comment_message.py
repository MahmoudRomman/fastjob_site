# Generated by Django 4.2.5 on 2023-10-09 10:40

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
