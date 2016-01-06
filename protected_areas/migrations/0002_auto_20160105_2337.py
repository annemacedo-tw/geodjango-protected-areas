# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protected_areas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='protectedareabrasil',
            name='group',
        ),
        migrations.AddField(
            model_name='baseprotectedarea',
            name='type',
            field=models.CharField(max_length=254, blank=True, null=True),
        ),
    ]
