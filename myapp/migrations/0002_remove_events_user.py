# Generated by Django 3.0 on 2020-08-31 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='user',
        ),
    ]
