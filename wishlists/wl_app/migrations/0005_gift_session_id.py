# Generated by Django 4.1.5 on 2023-02-08 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wl_app', '0004_gift'),
    ]

    operations = [
        migrations.AddField(
            model_name='gift',
            name='session_id',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Идентификатор сессии'),
        ),
    ]