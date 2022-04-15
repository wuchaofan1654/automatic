# Generated by Django 2.2.16 on 2022-03-28 03:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import frames.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', frames.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('modifier', frames.fields.ModifierCharField(blank=True, help_text='该记录最后修改者', max_length=255, null=True, verbose_name='修改者')),
                ('dept_belong_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='数据归属部门')),
                ('update_datetime', frames.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', frames.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('cpu_num', models.CharField(max_length=8, verbose_name='CPU核数')),
                ('cpu_sys', models.CharField(max_length=8, verbose_name='CPU已使用率')),
                ('mem_num', models.CharField(max_length=32, verbose_name='内存总数(KB)')),
                ('mem_sys', models.CharField(max_length=32, verbose_name='内存已使用大小(KB)')),
                ('seconds', models.CharField(max_length=32, verbose_name='系统已运行时间')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
            ],
            options={
                'verbose_name': '服务器监控信息',
                'verbose_name_plural': '服务器监控信息',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='服务器名称')),
                ('ip', models.CharField(max_length=32, verbose_name='ip地址')),
                ('os', models.CharField(max_length=32, verbose_name='操作系统')),
                ('remark', models.CharField(blank=True, max_length=256, null=True, verbose_name='备注')),
                ('update_datetime', frames.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', frames.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '服务器信息',
                'verbose_name_plural': '服务器信息',
            },
        ),
        migrations.CreateModel(
            name='SysFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', frames.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('modifier', frames.fields.ModifierCharField(blank=True, help_text='该记录最后修改者', max_length=255, null=True, verbose_name='修改者')),
                ('dept_belong_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='数据归属部门')),
                ('update_datetime', frames.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', frames.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('dir_name', models.CharField(max_length=32, verbose_name='磁盘路径')),
                ('sys_type_name', models.CharField(max_length=400, verbose_name='系统文件类型')),
                ('type_name', models.CharField(max_length=32, verbose_name='盘符类型')),
                ('total', models.CharField(max_length=32, verbose_name='磁盘总大小(KB)')),
                ('disk_sys', models.CharField(max_length=32, verbose_name='已使用大小(KB)')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
                ('monitor', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='monitor.Monitor', verbose_name='关联服务器监控信息')),
            ],
            options={
                'verbose_name': '系统磁盘',
                'verbose_name_plural': '系统磁盘',
            },
        ),
        migrations.AddField(
            model_name='monitor',
            name='server',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='monitor.Server', verbose_name='关联服务器信息'),
        ),
    ]
