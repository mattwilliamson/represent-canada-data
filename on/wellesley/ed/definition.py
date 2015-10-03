from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Wellesley wards',
    domain='Wellesley, ON',
    last_updated=date(2015, 1, 6),
    name_func=boundaries.attr('WardName'),
    id_func=boundaries.attr('WardNumber'),
    authority='Regional Municipality of Waterloo',
    source_url='http://www.regionofwaterloo.ca/en/regionalGovernment/WardBoundaries.asp',
    licence_url='http://www.regionofwaterloo.ca/en/regionalGovernment/OpenDataLicence.asp',
    data_url='http://www.regionofwaterloo.ca/opendatadownloads/WardBoundaries.zip',
    encoding='iso-8859-1',
    metadata={'geographic_code': '3530027'},
    ogr2ogr='''-where "Municipali='Wellesley'"''',
    skip_crc32=True,
)
