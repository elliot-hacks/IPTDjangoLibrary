# Generated by Django 4.2.4 on 2023-08-24 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
        migrations.RenameModel(
            old_name='Collections',
            new_name='Collection',
        ),
    ]
