# Generated by Django 4.1.7 on 2023-04-03 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0009_remove_projects_project_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='project_subtitle',
            field=models.CharField(default='', max_length=512),
            preserve_default=False,
        ),
    ]