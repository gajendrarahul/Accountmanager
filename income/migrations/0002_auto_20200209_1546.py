# Generated by Django 3.0.2 on 2020-02-09 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Expenses',
            new_name='Income',
        ),
    ]
