# Generated by Django 4.1.7 on 2023-03-21 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_technicalskills'),
    ]

    operations = [
        migrations.AddField(
            model_name='technicalskills',
            name='skill_type',
            field=models.IntegerField(choices=[(1, 'Language'), (2, 'Framework'), (3, 'Database'), (4, 'Tool')], default=1),
            preserve_default=False,
        ),
    ]
