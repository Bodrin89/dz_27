# Generated by Django 4.1.5 on 2023-02-09 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='location_id',
            new_name='location',
        ),
    ]