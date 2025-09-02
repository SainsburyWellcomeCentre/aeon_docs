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

```{note}
The links to the "raw" datasets are temporarily unavailable while we resolve access issues. 
Please check back later or reach out to the [project maintainers](target-project-maintainers) if you need urgent access.
```

These datasets contain complete experimental recordings captured across multiple acquisition machines, with sizes generally in the **terabyte (TB)** range.
Each dataset is labelled by the experiment name (e.g. `social0.2`) followed by the name of the acquisition machine (e.g. `aeon3`).

"raw" datasets include [raw data](target-data-provenance-raw) acquired from _all_ streams used in an experiment, while "ingest" datasets contain only a _subset_ of post-processed, [derived data](target-data-provenance-derived) (typically full-pose position and/or weight data).
For most analyses, using both "raw" and "ingest" datasets provides the cleanest and most complete view. 

- **social0.2-aeon3**: [raw](), [ingest](https://app.globus.org/file-manager?origin_id=35289aa3-af85-44aa-8f95-16167a47fde4&origin_path=%2F)

- **social0.2-aeon4**: [raw](), [ingest](https://app.globus.org/file-manager?origin_id=ca754f8a-e774-4aa8-b52e-2137d268764d&origin_path=%2F)

- **social0.3-aeon3**: [raw](), [ingest](https://app.globus.org/file-manager?origin_id=37ce19e9-e0d1-41cb-b29d-51ca7a09d768&origin_path=%2F)

- **social0.4-aeon3**: [raw](), [ingest](https://app.globus.org/file-manager?origin_id=fd732cba-fbda-47f5-810f-35fca21582e1&origin_path=%2F)

- **social0.4-aeon4**: [raw](), [ingest](https://app.globus.org/file-manager?origin_id=fd732cba-fbda-47f5-810f-35fca21582e1&origin_path=%2F)

(target-precomputed-datasets)=
## Precomputed datasets
These datasets contain outputs derived from full datasets that have already been run through the upstream pipelines.
Stored in compact formats (e.g. Parquet, pickle), they are designed to support tutorials and how-to guides without requiring users to re-run heavy preprocessing or analysis steps.
While downstream of "raw" and "ingest", they prioritise ease of use and clarity of analysis over full provenance traceability.

- [**Platform paper social analysis datasets**](https://app.globus.org/file-manager?origin_id=2c09d69d-8ba0-4ca4-9762-7c784949e5c1&origin_path=%2F
): Datasets analysed in the [platform paper](aeon-paper:) social experiments.
- [**Filtered mouse position data**](https://app.globus.org/file-manager?origin_id=65b637ce-8146-4305-8cb8-d87b526a9ff6&origin_path=%2F): Position and kinematic data from a two-hour snippet of a single mouse in a foraging assay.