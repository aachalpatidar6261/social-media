# Generated by Django 4.2.3 on 2023-07-29 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_doctors', '0004_alter_signup_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='profile_pic',
            field=models.ImageField(default='', upload_to='profile/'),
        ),
    ]