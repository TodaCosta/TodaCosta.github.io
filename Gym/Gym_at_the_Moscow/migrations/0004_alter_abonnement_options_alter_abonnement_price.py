# Generated by Django 4.0.2 on 2022-04-11 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gym_at_the_Moscow', '0003_abonnement'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='abonnement',
            options={'verbose_name': 'Абонемент', 'verbose_name_plural': 'Абонементы'},
        ),
        migrations.AlterField(
            model_name='abonnement',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена, руб.'),
        ),
    ]
