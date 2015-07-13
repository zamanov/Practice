# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serv', '0003_auto_20150713_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='cell',
            name='is_blocked',
            field=models.BooleanField(default=False),
        ),
    ]
