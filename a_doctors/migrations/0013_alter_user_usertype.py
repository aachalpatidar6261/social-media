# Generated by Django 4.2.4 on 2023-09-12 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_doctors', '0012_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='usertype',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
