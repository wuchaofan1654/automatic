# Generated by Django 2.2.16 on 2022-04-19 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='key_yn',
            field=models.IntegerField(choices=[(1, '是'), (0, '否')], default=0, verbose_name='是否核心接口'),
        ),
        migrations.AlterField(
            model_name='api',
            name='method',
            field=models.IntegerField(choices=[(1, 'GET'), (2, 'POST'), (3, 'PUT'), (4, 'DELETE')], default=1, verbose_name='请求方式'),
        ),
    ]