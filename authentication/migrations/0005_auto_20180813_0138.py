# Generated by Django 2.0.7 on 2018-08-13 06:38

import authentication.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20180813_0130'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
                ('objects', authentication.models.AccountManager()),
            ],
        ),
    ]
