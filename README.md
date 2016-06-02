# Represent API: Data

[Represent](https://represent.opennorth.ca/) is the open database of Canadian elected officials and electoral districts. It provides a [REST API](https://represent.opennorth.ca/api/) to boundary, representative, and postcode resources.

This repository stores the digital boundary files for the database. The [represent-canada](https://github.com/opennorth/represent-canada) repository is what's running at [represent.opennorth.ca](https://represent.opennorth.ca/).

## License

Open North has permission to redistribute all datasets in this repository. Please read the [overall license](https://github.com/opennorth/represent-canada-data/tree/master/LICENSE.txt) and the `LICENSE.txt` file in each directory to know your rights. In some cases, you will not have permission to redistribute the dataset.

## Data Quality

### Lineage

All datasets are from government sources, with one exception: the postal code<sup>OM</sup> dataset in the `postcodes/fed` directory is from [Geocoder.ca](http://geocoder.ca/). ([Canada Post has sued Geocoder.ca](http://geocoder.ca/?sued=1) for distributing this file.) The `definition.py` files will have more details on sources and any modifications made to the files. Postal Code<sup>OM</sup> is an official mark of Canada Post Corporation.

### Completeness

We do not have permission to redistribute every dataset available through the [Represent API](https://represent.opennorth.ca/api/). For example, we do not have permission from the Government of Ontario to distribute its [boundary file](http://www.elections.on.ca/en-CA/Tools/ElectoralDistricts/Shapefile.htm) and [postal code<sup>OM</sup> concordance file](http://www.elections.on.ca/en-CA/Tools/ElectoralDistricts/PostalCodeFile.htm) (no longer available). You must download these files separately from Elections Ontario. You may then use the `definition.py` file we provide to load it into the database.

## Maintenance

### One-time setup

    # Invoke must not be installed globally.
    pip uninstall invoke
    # Create a virtual environment.
    mkvirtualenv representdata
    # Install the requirements.
    pip install -r requirements.txt

### Regular tasks

Load the virtual environment:

    workon representdata

Check that all `definition.py` files are valid:

    invoke definitions

Check that the source, data and license URLs work:

    invoke urls

Check that all data directories contain a `LICENSE.txt`:

    invoke licenses

Update any out-of-date shapefiles:

    invoke shapefiles

Or update a specific shapefile:

    invoke shapefiles --base=boundaries/ocd-division/country:ca/province:qc

Fix file permissions:

    invoke permissions

Check if the data request process spreadsheet is out-of-date:

    invoke spreadsheet

## Contact

Please use [GitHub Issues](https://github.com/opennorth/represent-canada-data/issues) for bug reports. You may also contact [represent@opennorth.ca](mailto:represent@opennorth.ca).

## Acknowledgements

We would like to express our gratitude to [Kent Mewhort](http://www.openissues.ca/) at the [Canadian Internet Policy and Public Interest Clinic (CIPPIC)](https://cippic.ca/), whose [legal research](https://cippic.ca/en/open_governance) ([PDF](https://cippic.ca/en/publications/how_to_redistribute_open_data)) made it possible for this repository to be made public.
