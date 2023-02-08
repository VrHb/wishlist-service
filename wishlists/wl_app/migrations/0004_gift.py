# Generated by Django 4.1.5 on 2023-02-08 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wl_app', '0003_wish_is_given'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название подарка')),
                ('link', models.CharField(blank=True, max_length=300, null=True, verbose_name='Ссылка')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Цена')),
            ],
        ),
    ]