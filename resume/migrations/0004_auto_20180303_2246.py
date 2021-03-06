# Generated by Django 2.0.2 on 2018-03-04 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20180303_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='level',
            field=models.CharField(choices=[(5, 'Native'), (4, 'Full professional proficiency'), (3, 'Professional working proficiency'), (2, 'Limited professional proficiency'), (1, 'Elementary professional proficiency')], default=5, help_text='Choice between 1 and 5', max_length=25),
        ),
    ]
