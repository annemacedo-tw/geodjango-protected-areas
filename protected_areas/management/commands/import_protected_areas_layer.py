from django.core.management.base import BaseCommand
from django.contrib.gis.utils import LayerMapping
from protected_areas.models import ProtectedArea


class Command(BaseCommand):
    help = 'Import village layer'

    def add_arguments(self, parser):
        parser.add_argument('shapefile_path', nargs='+', type=str)

    def handle(self, *args, **options):

        protected_areas_mapping = {
            'id_uc' : 'ID_UC0',
            'name' : 'NOME_UC1',
            'id_wcmc2' : 'ID_WCMC2',
            'category' : 'CATEGORI3',
            'group' : 'GRUPO4',
            'esfera5' : 'ESFERA5',
            'creation_year' : 'ANO_CRIA6',
            'gid7' : 'GID7',
            'precision' : 'QUALIDAD8',
            'legal_act' : 'ATO_LEGA9',
            'dt_ultim10' : 'DT_ULTIM10',
            'codigo_u11' : 'CODIGO_U11',
            'org_name' : 'NOME_ORG12',
            'geometry' : 'MULTIPOLYGON',
            # 'geometry' : 'POLYGON',
        }

        shapefile_path = options['shapefile_path'][0]

        lm = LayerMapping(ProtectedArea, shapefile_path, protected_areas_mapping,
                          transform=True, encoding='iso-8859-1')

        lm.save(strict=True, verbose=True)

        self.stdout.write('Successfull imported Protected areas! Path: "%s"' % shapefile_path)
