# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseProtectedArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='name')),
                ('category', models.CharField(blank=True, null=True, max_length=254)),
                ('creation_year', models.CharField(blank=True, null=True, max_length=254)),
                ('country', models.CharField(blank=True, null=True, max_length=254)),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='ProtectedAreaBrasil',
            fields=[
                ('baseprotectedarea_ptr', models.OneToOneField(serialize=False, to='protected_areas.BaseProtectedArea', parent_link=True, primary_key=True, auto_created=True)),
                ('id_uc', models.CharField(blank=True, null=True, max_length=254)),
                ('id_wcmc2', models.CharField(blank=True, null=True, max_length=254)),
                ('group', models.CharField(blank=True, null=True, max_length=254)),
                ('esfera5', models.CharField(blank=True, null=True, max_length=254)),
                ('gid7', models.CharField(blank=True, null=True, max_length=254)),
                ('precision', models.CharField(blank=True, null=True, max_length=254)),
                ('legal_act', models.CharField(blank=True, null=True, max_length=254)),
                ('dt_ultim10', models.CharField(blank=True, null=True, max_length=254)),
                ('codigo_u11', models.CharField(blank=True, null=True, max_length=254)),
                ('org_name', models.CharField(blank=True, null=True, max_length=254)),
            ],
            bases=('protected_areas.baseprotectedarea',),
        ),
    ]
