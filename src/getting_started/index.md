(target-repositories)=
# Getting Started

## Introduction to Project Aeon

## Repositories

:::{important}
You must be an SWC Github 'aeon' project member to view some of these repositories.
:::

::::{grid} 1 2 2 2
:gutter: 3 

:::{grid-item-card} {fas}`database;sd-text-primary` aeon_mecha
:link: https://github.com/SainsburyWellcomeCentre/aeon_mecha
:link-type: url
Project Aeon's main library for interfacing with acquired data
:::

:::{grid-item-card} {fas}`flask;sd-text-primary` aeon_experiments
:link: https://github.com/SainsburyWellcomeCentre/aeon_experiments
:link-type: url
Aeon experiment workflows written in the Bonsai visual programming language
:::

:::{grid-item-card} {fas}`computer;sd-text-primary` aeon_acquisition
:link: https://github.com/SainsburyWellcomeCentre/aeon_acquisition
:link-type: url
Source code for the 'aeon_acquisition' Bonsai package used in Aeon experiment workflows
:::

:::{grid-item-card} {fas}`chart-line;sd-text-primary` aeon_analysis
:link: https://github.com/SainsburyWellcomeCentre/aeon_analysis
:link-type: url
Python modules for analysis of Aeon experiment data
:::

:::{grid-item-card} {fas}`gear;sd-text-primary` aeon_lineardrive
:link: https://github.com/SainsburyWellcomeCentre/aeon_lineardrive
:link-type: url
Source code for actuating a linear drive motor used in Aeon experiments
:::

:::{grid-item-card} {fas}`cookie-bite;sd-text-primary` aeon_feeder
:link: https://github.com/SainsburyWellcomeCentre/aeon_feeder
:link-type: url
Source code for pellet delivery via feeders used in Aeon experiments
:::
::::

:::{note}
All experiment data is acquired and/or triggered and/or synced by [Harp devices](https://www.cf-hw.org/harp). Code in the 'aeon_acquisition' and 'aeon_mecha' repos makes use of the [Harp protocol](harp-tech:articles/about) during data acquisition, raw data file writing, and raw data file reading. See also the documentation on [Harp device operation and common registers](harp-tech:protocol/Device), the [Harp binary protocol](harp-tech:protocol/BinaryProtocol-8bit), and [Harp clock synchronization](harp-tech:protocol/SynchronizationClock).
:::