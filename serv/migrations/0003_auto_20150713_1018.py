# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serv', '0002_object_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='cell',
            name='row',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cell',
            name='sector',
            field=models.IntegerField(default=0),
        ),
    ]
