# Generated by Django 3.1.5 on 2021-03-02 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0024_auto_20210301_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='common_change',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='common_change_perc',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='common_price',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='common_volume',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='rights_change',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='rights_change_perc',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='rights_price',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='rights_volume',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='unit_change',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='unit_change_perc',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='unit_volume',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='warrant_change',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='warrant_change_perc',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='warrant_price',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='warrant_volume',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
