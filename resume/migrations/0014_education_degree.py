# Generated by Django 2.0.2 on 2018-02-25 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0013_personalinfo_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='degree',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
