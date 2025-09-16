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

- **Social 0.2**: A foraging assay with three food patches featuring dynamically varying reward rates. Each experiment consists of three periods: _presocial_ (each mouse alone for 3–4 days), _social_ (both mice together for 2 weeks), and _postsocial_ (each mouse alone again for 3–4 days).
    - **social0.2-aeon3**: [raw](https://app.globus.org/file-manager?origin_id=18397e02-9a8e-468e-9494-7f80a41727e5), [ingest](https://app.globus.org/file-manager?origin_id=1ab867b9-abf7-4494-bc01-42c57ebcaff4)
    - **social0.2-aeon4**: [raw](https://app.globus.org/file-manager?origin_id=6dff8570-881d-4116-9c69-4495711be44b), [ingest](https://app.globus.org/file-manager?origin_id=ba50f5c9-9702-487a-884c-2707507571d0)
- **Social 0.3/0.4**: A variant of the `social 0.2` assay, with three food patches and one dummy patch fixed at the center of the habitat. The reward-rate combinations span a wider range, and the habitat includes two additional gates connecting the outer corridor to the main area. Two wooden balls are also provided as enrichment for the mice to push around. The same three-period structure (_presocial_, _social_, _postsocial_) is used.
    - **social0.3-aeon3**: [raw](https://app.globus.org/file-manager?origin_id=788472a1-da5b-41ad-ae2a-855158b9d23d), [ingest](https://app.globus.org/file-manager?origin_id=ebee46d0-e1f8-4389-bd95-0006d1faf542)

    - **social0.4-aeon3**: [raw](https://app.globus.org/file-manager?origin_id=e85c1626-e845-4224-9ec9-6e3465abbb2a), [ingest](https://app.globus.org/file-manager?origin_id=9fcdfb0c-888b-49a6-9891-ca1c6e3fd6a1)

    - **social0.4-aeon4**: [raw](https://app.globus.org/file-manager?origin_id=a9304184-c573-409c-b161-ddf10ccdacef), [ingest](https://app.globus.org/file-manager?origin_id=69f23a6e-f9de-487e-8dda-a27e9ba7faeb)

(target-precomputed-datasets)=
## Precomputed datasets
These datasets contain outputs derived from full datasets that have already been run through the upstream pipelines.
Stored in compact formats (e.g. Parquet, pickle), they are designed to support tutorials and how-to guides without requiring users to re-run heavy preprocessing or analysis steps.
While downstream of "raw" and "ingest", they prioritise ease of use and clarity of analysis over full provenance traceability.

- [**Platform paper social analysis datasets**](https://app.globus.org/file-manager?origin_id=2c09d69d-8ba0-4ca4-9762-7c784949e5c1
): Datasets analysed in the [platform paper](aeon-paper:) social experiments.
- [**Filtered mouse position data**](https://app.globus.org/file-manager?origin_id=65b637ce-8146-4305-8cb8-d87b526a9ff6): Position and kinematic data from a two-hour snippet of a single mouse in a foraging assay.