# Generated by Django 2.0.2 on 2018-03-04 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slackbot', '0002_auto_20180227_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crontab',
            name='channel_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]