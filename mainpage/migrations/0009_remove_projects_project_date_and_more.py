# Generated by Django 4.1.7 on 2023-04-03 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0008_projects_project_stub'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='project_date',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='project_description',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='project_stub',
        ),
        migrations.AlterField(
            model_name='technicalskills',
            name='skill_type',
            field=models.IntegerField(choices=[(1, 'Languages'), (2, 'Frameworks/Libraries'), (3, 'Databases'), (4, 'Tools')]),
        ),
    ]
