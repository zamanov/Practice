# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='object',
            name='owner',
            field=models.CharField(default=b'admin', max_length=30),
        ),
    ]
