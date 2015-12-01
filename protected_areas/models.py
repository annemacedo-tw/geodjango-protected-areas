from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _


# Unidade de Conservação
class ProtectedArea(models.Model):
    id_uc = models.CharField(max_length=254)
    name = models.CharField(_('name'), max_length=254)
    id_wcmc2 = models.CharField(max_length=254)
    category = models.CharField(max_length=254)
    group = models.CharField(max_length=254)
    esfera5 = models.CharField(max_length=254)
    creation_year = models.CharField(max_length=254)
    gid7 = models.CharField(max_length=254)
    precision = models.CharField(max_length=254)
    legal_act = models.CharField(max_length=254)
    dt_ultim10 = models.CharField(max_length=254)
    codigo_u11 = models.CharField(max_length=254)
    org_name = models.CharField(max_length=254)
    geometry = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()
