# Generated by Django 4.1.5 on 2024-05-06 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wl_app', '0004_alter_wish_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='link',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='Ссылка'),
        ),
    ]
