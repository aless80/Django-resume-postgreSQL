# Generated by Django 2.0.2 on 2018-03-03 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_programminglanguage_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='skillurl',
        ),
    ]