# Generated by Django 3.0.7 on 2020-06-22 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20200622_0616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='fullname',
            new_name='fname',
        ),
    ]