# Generated by Django 3.0.2 on 2020-02-11 10:32

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0002_auto_20200209_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='expenses/'),
        ),
        migrations.AlterField(
            model_name='income',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title'),
        ),
        migrations.AlterField(
            model_name='incomecategory',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title'),
        ),
    ]
