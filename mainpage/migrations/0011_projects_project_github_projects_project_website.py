# Generated by Django 4.1.7 on 2023-04-03 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0010_projects_project_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='project_github',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='project_website',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]