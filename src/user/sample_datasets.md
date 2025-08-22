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
The links to the full datasets are temporarily unavailable while we resolve access issues. 
Please check back later or reach out to the [project maintainers](target-project-maintainers) if you need urgent access.
```

These datasets contain complete experimental recordings captured across multiple acquisition machines, with sizes generally in the **terabyte (TB)** range.
Each dataset is labelled by the experiment name (e.g. `social0.2`) followed by the name of the acquisition machine (e.g. `aeon3`).

"raw" datasets include [raw data](target-data-provenance-raw) acquired from _all_ streams used in an experiment, while "ingest" datasets contain only a _subset_ of post-processed, [derived data](target-data-provenance-derived) (typically full-pose position and/or weight data).
For most analyses, using both "raw" and "ingest" datasets provides the cleanest and most complete view. 

- **social0.2-aeon3** 
- **social0.2-aeon4**
- **social0.3-aeon3**
- **social0.3-aeon4**
- **social0.4-aeon3**
- **social0.4-aeon4**

(target-precomputed-datasets)=
## Precomputed datasets
These datasets contain outputs derived from full datasets that have already been run through the upstream pipelines.
Stored in compact formats (e.g. Parquet, pickle), they are designed to support tutorials and how-to guides without requiring users to re-run heavy preprocessing or analysis steps.
While downstream of "raw" and "ingest", they prioritise ease of use and clarity of analysis over full provenance traceability.

- [**Platform paper social analysis datasets**](https://app.globus.org/file-manager?origin_id=48cc1398-b591-4f52-85d2-f68801306d4a&origin_path=%2F): Datasets analysed in the [platform paper](aeon-paper:) social experiments.
- [**Filtered mouse position data**](../../downloads/hmm_example_mouse_pos.pkl): Position and kinematic data from a two-hour snippet of a single mouse in a foraging assay.