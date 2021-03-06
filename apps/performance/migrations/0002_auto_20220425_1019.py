# Generated by Django 2.2.16 on 2022-04-25 02:19

from django.db import migrations, models
import frames.fields


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=1, verbose_name='状态')),
                ('description', frames.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('update_datetime', frames.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', frames.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('name', models.CharField(default='', max_length=50, verbose_name='版本名称')),
            ],
            options={
                'verbose_name': '发布版本表',
                'verbose_name_plural': '发布版本表',
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='module',
            name='version',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='publish',
            unique_together=set(),
        ),
    ]
