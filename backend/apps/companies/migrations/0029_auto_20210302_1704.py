# Generated by Django 3.1.5 on 2021-03-02 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0028_auto_20210302_1658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commonquote',
            old_name='common',
            new_name='company',
        ),
    ]
