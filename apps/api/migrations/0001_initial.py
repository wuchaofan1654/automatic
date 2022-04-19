# Generated by Django 2.2.16 on 2022-04-19 03:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import frames.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('permission', '0003_remove_module_dept'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', frames.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('modifier', frames.fields.ModifierCharField(blank=True, help_text='该记录最后修改者', max_length=255, null=True, verbose_name='修改者')),
                ('dept_belong_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='数据归属部门')),
                ('update_datetime', frames.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', frames.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('name', models.CharField(default='', max_length=255, unique=True, verbose_name='接口名称(unique)')),
                ('url', models.CharField(default='', max_length=255, verbose_name='接口路径(不带host)')),
                ('method', models.CharField(default='', max_length=255, verbose_name='请求方式')),
                ('key_yn', models.IntegerField(default='', max_length=255, verbose_name='是否核心接口')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
                ('dept', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='permission.Dept', verbose_name='所属团队')),
            ],
            options={
                'verbose_name': '接口主表',
                'verbose_name_plural': '接口主表',
            },
        ),
        migrations.CreateModel(
            name='Validator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', frames.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('modifier', frames.fields.ModifierCharField(blank=True, help_text='该记录最后修改者', max_length=255, null=True, verbose_name='修改者')),
                ('dept_belong_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='数据归属部门')),
                ('update_datetime', frames.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', frames.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('expression', models.CharField(default='', max_length=255, verbose_name='验证表达式')),
                ('expression_type', models.IntegerField(choices=[(1, 'Json 路径'), (2, '正则表达式'), (3, 'Mysql表达式')], default=1, verbose_name='表达式类型')),
                ('excepted', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='期望值')),
                ('symbol', models.CharField(choices=[('=', 'equals'), ('str=', 'equals as str'), ('int=', 'equals as int'), ('in', 'in'), ('not in', 'not in'), ('contains', 'contains'), ('not contains', 'not contains'), ('is null', 'is null'), ('not null', 'not null')], default='=', max_length=50, verbose_name='比较符')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
            ],
            options={
                'verbose_name': '验证器',
                'verbose_name_plural': '验证器',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', frames.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('modifier', frames.fields.ModifierCharField(blank=True, help_text='该记录最后修改者', max_length=255, null=True, verbose_name='修改者')),
                ('dept_belong_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='数据归属部门')),
                ('update_datetime', frames.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', frames.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('message', models.TextField(default='succeed', verbose_name='执行结果')),
                ('api', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.Api', verbose_name='关联接口')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
            ],
            options={
                'verbose_name': '接口执行结果',
                'verbose_name_plural': '接口执行结果',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', frames.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('modifier', frames.fields.ModifierCharField(blank=True, help_text='该记录最后修改者', max_length=255, null=True, verbose_name='修改者')),
                ('dept_belong_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='数据归属部门')),
                ('update_datetime', frames.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', frames.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
                ('results', models.ManyToManyField(to='api.Result', verbose_name='关联结果')),
            ],
            options={
                'verbose_name': '执行报告',
                'verbose_name_plural': '执行报告',
            },
        ),
        migrations.CreateModel(
            name='Param',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', frames.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('modifier', frames.fields.ModifierCharField(blank=True, help_text='该记录最后修改者', max_length=255, null=True, verbose_name='修改者')),
                ('dept_belong_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='数据归属部门')),
                ('update_datetime', frames.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', frames.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('key', models.CharField(default='', max_length=255, verbose_name='参数名称')),
                ('value', models.CharField(default='', max_length=255, verbose_name='参数值')),
                ('type', models.IntegerField(choices=[(1, 'str'), (2, 'int'), (3, 'list'), (4, 'dict'), (5, 'file')], default=1, verbose_name='参数类型')),
                ('require', models.IntegerField(choices=[(1, '必填'), (2, '非必填')], default=0, verbose_name='是否必填')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
            ],
            options={
                'verbose_name': '请求参数表',
                'verbose_name_plural': '请求参数表',
            },
        ),
        migrations.CreateModel(
            name='Extractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', frames.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('modifier', frames.fields.ModifierCharField(blank=True, help_text='该记录最后修改者', max_length=255, null=True, verbose_name='修改者')),
                ('dept_belong_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='数据归属部门')),
                ('update_datetime', frames.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', frames.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('expression', models.CharField(default='', max_length=255, verbose_name='提取表达式')),
                ('expression_type', models.IntegerField(choices=[(1, 'Json 路径'), (2, '正则表达式'), (3, 'Mysql表达式')], default=1, verbose_name='表达式类型')),
                ('variable', models.CharField(default='', max_length=255, verbose_name='赋值变量名')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
            ],
            options={
                'verbose_name': '提取器',
                'verbose_name_plural': '提取器',
            },
        ),
        migrations.AddField(
            model_name='api',
            name='extractors',
            field=models.ManyToManyField(to='api.Extractor', verbose_name='关联提取器'),
        ),
        migrations.AddField(
            model_name='api',
            name='module',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='permission.Module', verbose_name='关联模块'),
        ),
        migrations.AddField(
            model_name='api',
            name='params',
            field=models.ManyToManyField(to='api.Param', verbose_name='关联参数'),
        ),
        migrations.AddField(
            model_name='api',
            name='validators',
            field=models.ManyToManyField(to='api.Validator', verbose_name='关联验证器'),
        ),
    ]