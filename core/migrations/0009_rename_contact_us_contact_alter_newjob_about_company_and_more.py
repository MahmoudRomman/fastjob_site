# Generated by Django 4.2.5 on 2023-10-05 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_newjob_about_company'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact_Us',
            new_name='Contact',
        ),
        migrations.AlterField(
            model_name='newjob',
            name='about_company',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='newjob',
            name='job_description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='newjob',
            name='qualifications',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='newjob',
            name='responsibility',
            field=models.TextField(max_length=1000),
        ),
    ]