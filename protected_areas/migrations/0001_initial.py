# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseProtecdArea',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='name', max_length=254)),
                ('category', models.CharField(null=True, blank=True, max_length=254)),
                ('creation_year', models.CharField(null=True, blank=True, max_length=254)),
                ('country', models.CharField(null=True, blank=True, max_length=254)),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='ProtectedAreaBrasil',
            fields=[
                ('baseprotecdarea_ptr', models.OneToOneField(serialize=False, auto_created=True, primary_key=True, parent_link=True, to='protected_areas.BaseProtecdArea')),
                ('id_uc', models.CharField(null=True, blank=True, max_length=254)),
                ('id_wcmc2', models.CharField(null=True, blank=True, max_length=254)),
                ('group', models.CharField(null=True, blank=True, max_length=254)),
                ('esfera5', models.CharField(null=True, blank=True, max_length=254)),
                ('gid7', models.CharField(null=True, blank=True, max_length=254)),
                ('precision', models.CharField(null=True, blank=True, max_length=254)),
                ('legal_act', models.CharField(null=True, blank=True, max_length=254)),
                ('dt_ultim10', models.CharField(null=True, blank=True, max_length=254)),
                ('codigo_u11', models.CharField(null=True, blank=True, max_length=254)),
                ('org_name', models.CharField(null=True, blank=True, max_length=254)),
            ],
            bases=('protected_areas.baseprotecdarea',),
        ),
    ]
