# Generated by Django 2.1.7 on 2019-02-24 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eip', '0003_eip_voting_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eip',
            name='eip_num',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
