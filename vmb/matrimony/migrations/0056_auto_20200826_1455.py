# Generated by Django 2.2.7 on 2020-08-26 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony', '0055_auto_20200826_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matrimonyprofile',
            name='father_status',
            field=models.CharField(blank=True, choices=[('EMP', 'Employed'), ('BUS', 'Business'), ('PRO', 'Professional'), ('RET', 'Retired'), ('NMP', 'Not Employed'), ('DEC', 'Deceased')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='matrimonyprofile',
            name='mother_status',
            field=models.CharField(blank=True, choices=[('HMK', 'Home Maker'), ('EMP', 'Employed'), ('BUS', 'Business'), ('PRO', 'Professional'), ('RET', 'Retired'), ('NMP', 'Not Employed'), ('DEC', 'Deceased')], max_length=3, null=True),
        ),
    ]
