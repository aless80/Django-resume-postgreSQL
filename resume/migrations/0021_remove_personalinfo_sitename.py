# Generated by Django 2.0.2 on 2018-03-02 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0020_personalinfo_facebook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalinfo',
            name='sitename',
        ),
    ]
