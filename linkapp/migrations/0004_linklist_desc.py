# Generated by Django 4.1 on 2022-10-26 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkapp', '0003_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='linklist',
            name='desc',
            field=models.CharField(max_length=200, null=True),
        ),
    ]