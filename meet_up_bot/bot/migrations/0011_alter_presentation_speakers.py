# Generated by Django 4.0.5 on 2022-08-07 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0010_alter_block_options_alter_flow_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='speakers',
            field=models.ManyToManyField(blank=True, related_name='presentations', to='bot.speaker', verbose_name='Спикер'),
        ),
    ]
