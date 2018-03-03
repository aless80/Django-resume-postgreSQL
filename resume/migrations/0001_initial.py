# Generated by Django 2.0.2 on 2018-03-03 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('order', models.IntegerField(default=1)),
                ('url', models.URLField(blank=True, verbose_name='School URL')),
                ('linkname', models.URLField(blank=True, default='')),
            ],
            options={
                'ordering': ['order', 'id'],
                'db_table': 'achievement',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('schoolurl', models.URLField(blank=True, verbose_name='School URL')),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('degree', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Education',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=250)),
                ('companyurl', models.URLField(verbose_name='Company URL')),
                ('location', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_current', models.BooleanField(default=False)),
                ('is_public', models.BooleanField(default=True)),
                ('company_image', models.CharField(blank=True, help_text='path to company image, local or otherwise', max_length=250)),
            ],
            options={
                'ordering': ['-end_date', '-start_date'],
                'db_table': 'jobs',
            },
        ),
        migrations.CreateModel(
            name='JobAccomplishment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('order', models.IntegerField(default=1)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Job')),
            ],
            options={
                'ordering': ['order', 'id'],
                'db_table': 'jobaccomplishment',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=20)),
                ('level', models.CharField(max_length=30)),
                ('ordering', models.IntegerField(default=1)),
            ],
            options={
                'ordering': ['ordering', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Overview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Overview',
            },
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(blank=True, max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('locality', models.CharField(help_text='e.g. city such as Boston', max_length=255)),
                ('region', models.CharField(blank=True, help_text='e.g. MA or Italy', max_length=255)),
                ('title', models.CharField(blank=True, help_text='e.g. Developer', max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('linkedin', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('github', models.URLField(blank=True)),
                ('site', models.URLField(blank=True)),
                ('twittername', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Personal Info',
            },
        ),
        migrations.CreateModel(
            name='ProgrammingLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('level', models.CharField(blank=True, max_length=50)),
                ('order', models.IntegerField(default=1)),
            ],
            options={
                'ordering': ['order', 'id'],
                'db_table': 'programminglanguage',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('skillurl', models.URLField(blank=True, verbose_name='Skill URL')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Skillset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='skill',
            name='skillset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Skillset'),
        ),
    ]
