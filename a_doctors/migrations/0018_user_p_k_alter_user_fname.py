# Generated by Django 4.2.4 on 2024-01-04 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('a_doctors', '0017_alter_user_fname_useractivity'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='p_k',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='fname',
            field=models.CharField(max_length=100),
        ),
    ]
