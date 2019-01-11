# Generated by Django 2.1.3 on 2019-01-02 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ethereum_client', '0002_votelog_votingdetailslog'),
        ('eip', '0002_auto_20181214_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='eip',
            name='voting_details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ethereum_client.VotingDetailsLog'),
        ),
    ]