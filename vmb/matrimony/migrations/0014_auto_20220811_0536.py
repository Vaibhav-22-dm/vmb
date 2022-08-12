# Generated by Django 2.2.7 on 2022-08-11 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony', '0013_auto_20220318_1651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matrimonyprofile',
            old_name='languages_read_write',
            new_name='languages_can_read_write',
        ),
        migrations.RenameField(
            model_name='matrimonyprofile',
            old_name='languages_known',
            new_name='languages_can_speak',
        ),
        migrations.AlterField(
            model_name='expectation',
            name='want_nri',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No'), ('', 'May be')], max_length=2, null=True, verbose_name='Do you want NRI'),
        ),
        migrations.AlterField(
            model_name='matrimonyprofile',
            name='status',
            field=models.CharField(blank=True, choices=[('00', 'Signup'), ('01', 'Registered'), ('02', 'Need more info'), ('10', 'Inactive'), ('11', 'Blocked'), ('20', 'Active'), ('30', 'In progress'), ('40', 'Matched'), ('50', 'QA'), ('60', 'Discussions'), ('90', 'Married externally'), ('99', 'Married')], default='00', max_length=2),
        ),
        migrations.AlterField(
            model_name='matrimonyprofile',
            name='want_children',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No'), ('', 'May be')], max_length=2, null=True, verbose_name='Do you want Children'),
        ),
    ]