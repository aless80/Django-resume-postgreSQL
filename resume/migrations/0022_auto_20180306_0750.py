# Generated by Django 2.0.2 on 2018-03-06 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0021_auto_20180305_2338'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgrammingArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('order', models.IntegerField(default=1)),
            ],
            options={
                'ordering': ['order', 'name'],
            },
        ),
        migrations.AddField(
            model_name='programminglanguage',
            name='programmingarea',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='resume.ProgrammingArea'),
            preserve_default=False,
        ),
    ]
