# Generated by Django 5.0.4 on 2024-04-19 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genshin_code_notifier', '0006_alter_code_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
