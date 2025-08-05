(target-sample-datasets)=
# Sample Datasets
To demonstrate Aeon's various features and capabilities, we also provide the following sample datasets that complement the user guide.

## Short datasets

- [**Single mouse in a foraging assay**](sample-data-single-mouse-foraging:): A two-hour snippet of a single mouse in a foraging assay consisting of three food patches. See [here](https://aeon.swc.ucl.ac.uk/user/how_to/io_api_example_copy.html) for example code to work with this dataset.

## Platform paper social experiment analyzed datasets (parquet files)

- [**Platform paper social experiment analyzed datasets**](https://app.globus.org/file-manager?origin_id=48cc1398-b591-4f52-85d2-f68801306d4a&origin_path=%2F): Datasets analyzed in the [platform paper](https://www.biorxiv.org/content/10.1101/2025.07.31.664513v1) social experiments as parquet files. See [here](https://aeon.swc.ucl.ac.uk/user/how_to/social_analysis1.html) and [here](https://aeon.swc.ucl.ac.uk/user/how_to/social_analysis2.html) for example code to work with these datasets.

## Platform paper social experiment full datasets

- **social0.2-aeon3**
    - [raw](https://app.globus.org/file-manager?origin_id=18397e02-9a8e-468e-9494-7f80a41727e5&origin_path=%2F)
    - [ingest](https://app.globus.org/file-manager?origin_id=35289aa3-af85-44aa-8f95-16167a47fde4&origin_path=%2F)

- **social0.2-aeon4**
    - [raw](https://app.globus.org/file-manager?origin_id=6dff8570-881d-4116-9c69-4495711be44b&origin_path=%2F)
    - [ingest](https://app.globus.org/file-manager?origin_id=ca754f8a-e774-4aa8-b52e-2137d268764d&origin_path=%2F)

- **social0.3-aeon3**
    - [raw](https://app.globus.org/file-manager?origin_id=788472a1-da5b-41ad-ae2a-855158b9d23d&origin_path=%2F)
    - [ingest](https://app.globus.org/file-manager?origin_id=37ce19e9-e0d1-41cb-b29d-51ca7a09d768&origin_path=%2F)

- **social0.3-aeon4**
    - [raw](https://app.globus.org/file-manager?origin_id=b317a669-5e62-4ecb-b322-072c0ffa5c0a&origin_path=%2F)
    - [ingest](https://app.globus.org/file-manager?origin_id=cb5d269f-d351-47aa-bfd1-c34ee4adec0a&origin_path=%2F)

- **social0.4-aeon3**
    - [raw](https://app.globus.org/file-manager?origin_id=e85c1626-e845-4224-9ec9-6e3465abbb2a&origin_path=%2F)
    - [ingest](https://app.globus.org/file-manager?origin_id=fd732cba-fbda-47f5-810f-35fca21582e1&origin_path=%2F)

- **social0.4-aeon4**
    - [raw](https://app.globus.org/file-manager?origin_id=a9304184-c573-409c-b161-ddf10ccdacef&origin_path=%2F)
    - [ingest](https://app.globus.org/file-manager?origin_id=fd732cba-fbda-47f5-810f-35fca21582e1&origin_path=%2F)

In [Aeon dataset terminology]((https://aeon.swc.ucl.ac.uk/about/design_considerations.html#data-provenance)), 'raw' datasets contain data acquired from _all_ streams used in an experiment, while 'ingest' datasets contain only _a small subset_ of raw data that has been further processed post-acquisition, to be optionally ingested into a database. For these experiments, 'ingest' typically only contains further processed full-pose position data and/or weight data.

If you want to use the "cleanest" data for a given experiment, you should use both the 'raw' and 'ingest' datasets. See [here](https://aeon.swc.ucl.ac.uk/user/how_to/io_api_example_copy.html) for example code to work with these datasets.