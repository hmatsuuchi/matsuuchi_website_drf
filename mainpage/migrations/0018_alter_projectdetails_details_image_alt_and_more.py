# Generated by Django 4.1.7 on 2023-04-18 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0017_projects_project_technologies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetails',
            name='details_image_alt',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projectdetails',
            name='details_image_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_image_alt',
            field=models.TextField(),
        ),
    ]