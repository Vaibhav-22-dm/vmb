# Generated by Django 2.2.7 on 2020-09-30 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony', '0069_auto_20200930_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matrimonyprofile',
            name='status',
            field=models.CharField(blank=True, choices=[('00', 'Signup'), ('01', 'Registered'), ('02', 'Need more info'), ('10', 'Inactive'), ('11', 'Blocked'), ('20', 'Active'), ('30', 'In progress'), ('40', 'Matched'), ('50', 'QA'), ('60', 'Discussions'), ('90', 'Married (outside sources)'), ('99', 'Married')], default='00', max_length=2),
        ),
    ]