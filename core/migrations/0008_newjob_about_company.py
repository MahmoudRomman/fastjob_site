# Generated by Django 4.2.5 on 2023-10-05 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_newjob_qualifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='newjob',
            name='about_company',
            field=models.TextField(default='wedfrtygfddddddddddddddddddddd'),
            preserve_default=False,
        ),
    ]