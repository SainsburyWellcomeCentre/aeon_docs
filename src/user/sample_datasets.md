(target-sample-datasets)=
# Sample Datasets
To demonstrate Aeon's various features and capabilities, we also provide the following datasets that complement the [tutorials](target-tutorials) and [how-to guides](target-how-to).

(target-short-datasets)=
## Short datasets
These lightweight datasets are curated excerpts from full experiments, typically sized in **gigabytes (GB)**.
They are selected to support quick inspection, pipeline prototyping, or tooling validation before committing to full dataset downloads.

- [**Single mouse in a foraging assay**](sample-data-single-mouse-foraging:): A two-hour snippet of a single mouse in a foraging assay consisting of three food patches.

(target-full-datasets)=
## Full datasets
These datasets contain complete experimental recordings captured across multiple acquisition machines, with sizes generally in the **terabyte (TB)** range.
Each dataset is labelled by the experiment name (e.g. `social0.2`) followed by the name of the acquisition machine (e.g. `aeon3`).

"raw" datasets include [raw data](target-data-provenance-raw) acquired from _all_ streams used in an experiment, while "ingest" datasets contain only a _subset_ of post-processed, [derived data](target-data-provenance-derived) (typically full-pose position and/or weight data).
For most analyses, using both "raw" and "ingest" datasets provides the cleanest and most complete view. 

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

(target-precomputed-datasets)=
## Precomputed datasets
These datasets contain outputs derived from full datasets that have already been run through the upstream pipelines.  
Stored in compact formats (e.g. Parquet, pickle), they are designed to support tutorials and how-to guides without requiring users to re-run heavy preprocessing or analysis steps.  
While downstream of "raw" and "ingest", they prioritise ease of use and clarity of analysis over full provenance traceability.  

- [**Platform paper social analysis datasets**](https://app.globus.org/file-manager?origin_id=48cc1398-b591-4f52-85d2-f68801306d4a&origin_path=%2F): Datasets analysed in the [platform paper](aeon-paper:) social experiments.
- [**Filtered mouse position data**](../../downloads/hmm_example_mouse_pos.pkl): Position and kinematic data from a two-hour snippet of a single mouse in a foraging assay.