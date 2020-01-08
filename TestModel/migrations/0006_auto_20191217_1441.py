# Generated by Django 2.2.7 on 2019-12-17 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0005_democtl'),
    ]

    operations = [
        migrations.AddField(
            model_name='democtl',
            name='demohost',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='democtl',
            name='demoport',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='democtl',
            name='demostate',
            field=models.CharField(default=1, max_length=16),
            preserve_default=False,
        ),
    ]