# Generated by Django 5.0.4 on 2024-04-11 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genshin_code_notifier', '0002_code_user_provider'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='provider',
            new_name='carrier',
        ),
    ]
