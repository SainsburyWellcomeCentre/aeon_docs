(target-repositories)=
# Repositories
The Aeon infrastructure is complex and multi-dimensional, spanning hardware, acquisition software, standard data formats, and a low-level API for data analysis. 
As each of these different components is built using different languages, including but not limited to CAD programs, [Bonsai](https://bonsai-rx.org/) and Python, we organise Aeon into the following repositories:

::::{grid} 1 2 2 2
:gutter: 3 

:::{grid-item-card} {fas}`computer;sd-text-primary` aeon_acquisition
:link: https://github.com/SainsburyWellcomeCentre/aeon_acquisition
:link-type: url
Source code for the `aeon_acquisition` Bonsai package used in 
Aeon experiment workflows.
:::

:::{grid-item-card} {fas}`file;sd-text-primary` aeon_api
:link: https://github.com/SainsburyWellcomeCentre/aeon_api
:link-type: url
Aeon's low-level library for interfacing with raw acquired data.
Contains modules for loading and processing raw data. 
:::

:::{grid-item-card} {fas}`book-atlas;sd-text-primary` aeon_docs
:link: https://github.com/SainsburyWellcomeCentre/aeon_docs
:link-type: url
Source code for the Aeon documentation site, built via Sphinx.
:::

:::{grid-item-card} {fas}`flask;sd-text-primary` aeon_experiments
:link: https://github.com/SainsburyWellcomeCentre/aeon_experiments
:link-type: url
Aeon experiment workflows written in the Bonsai visual programming language.
:::

:::{grid-item-card} {fas}`cookie-bite;sd-text-primary` aeon_feeder
:link: https://github.com/SainsburyWellcomeCentre/aeon_feeder
:link-type: url
Source code for pellet delivery via foraging patches used in Aeon experiments.
:::

:::{grid-item-card} {fas}`home;sd-text-primary` aeon_habitat
:link: https://github.com/SainsburyWellcomeCentre/aeon_habitat
:link-type: url
Contains the STEP file for the Aeon habitat and all its components.
:::

:::{grid-item-card} {fas}`gear;sd-text-primary` aeon_lineardrive
:link: https://github.com/SainsburyWellcomeCentre/aeon_lineardrive
:link-type: url
Source code for actuating a linear drive motor used in Aeon experiments.
:::

:::{grid-item-card} {fas}`database;sd-text-primary` aeon_mecha
:link: https://github.com/SainsburyWellcomeCentre/aeon_mecha
:link-type: url
Aeon's library for interfacing with the Aeon DataJoint pipeline.
Contains modules for data ingestion, processing, and analysis using DataJoint.
:::

:::{grid-item-card} {fas}`location-crosshairs;sd-text-primary` aeon_sleap_processing
:link: https://github.com/SainsburyWellcomeCentre/aeon_sleap_processing
:link-type: url
Aeon's pose and identity tracking pipeline using SLEAP.
:::

:::{grid-item-card} {fas}`lightbulb;sd-text-primary` aeon_template
:link: https://github.com/SainsburyWellcomeCentre/aeon_template
:link-type: url
Sample Aeon experiment workflow demonstrating a full acquisition pipeline.
:::
::::

:::{note}
All experiment data is acquired and/or triggered and/or synced by 
[Harp devices](https://www.cf-hw.org/harp). 
Code in the `aeon_acquisition` and `aeon_api` repositories makes use of 
the [Harp protocol](harp-tech:articles/about) during data acquisition, 
raw data file writing, and raw data file reading. 
See also the documentation on 
[Harp device operation and common registers](harp-tech:protocol/Device), 
the [Harp binary protocol](harp-tech:protocol/BinaryProtocol-8bit), and 
[Harp clock synchronisation](harp-tech:protocol/SynchronizationClock).
:::