# Generated by Django 2.2.16 on 2022-04-13 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True, auto_now=True)),
                ('version', models.CharField(default='', max_length=50)),
                ('build_no', models.CharField(default='', max_length=50)),
                ('branch', models.CharField(default='', max_length=255)),
                ('status', models.IntegerField(default=1)),
                ('jsonfile', models.FileField(default='', upload_to='files')),
            ],
            options={
                'verbose_name': '发布记录表',
                'verbose_name_plural': '发布记录表',
                'ordering': ['-id'],
                'unique_together': {('version', 'build_no', 'status')},
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True, auto_now=True)),
                ('module_name', models.CharField(default='', max_length=50)),
                ('module_size', models.IntegerField(default=0)),
                ('module_type', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=1)),
                ('publish', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='packageAnalyse.Publish')),
            ],
            options={
                'verbose_name': '模块大小表',
                'verbose_name_plural': '模块大小表',
                'ordering': ['-id'],
                'unique_together': {('publish', 'module_name')},
            },
        ),
    ]
