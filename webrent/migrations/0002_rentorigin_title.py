# Generated by Django 2.0.2 on 2018-09-25 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webrent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentorigin',
            name='title',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
