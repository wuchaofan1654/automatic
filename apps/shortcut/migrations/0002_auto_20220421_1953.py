# Generated by Django 2.2.16 on 2022-04-21 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortcut', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortcut',
            name='status',
            field=models.IntegerField(default=1, verbose_name='状态'),
        ),
        migrations.DeleteModel(
            name='Module',
        ),
    ]
