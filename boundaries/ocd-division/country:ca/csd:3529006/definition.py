from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Brantford wards',
    domain='Brantford, ON',
    last_updated=date(2012, 8, 20),
    name_func=boundaries.attr('WARD_NAME'),
    id_func=boundaries.attr('WARD'),
    authority='City of Brantford',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3529006'},
)