# Generated by Django 2.2.16 on 2022-04-19 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='status',
            field=models.IntegerField(default=1, verbose_name='状态'),
        ),
    ]