# Generated by Django 3.0.3 on 2020-06-19 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='priority',
            field=models.TextField(default=1995),
            preserve_default=False,
        ),
    ]
