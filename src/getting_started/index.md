(target-getting-started)=
# Getting Started

Aeon is an open-source platform designed to study the neural basis of natural behaviours over naturalistic timescales, from weeks to months. 
It features a modular, scalable, and programmable arena where animals live. 
Equipped with various [interactive and non-interactive modules](target-hardware) like feeders, nesting areas, microphones, RFID readers, and high-speed cameras, this setup mimics complex environments, allowing 
- animals to exhibit natural behaviours such as foraging, nesting, and social interaction, and
- continuous tracking of animal position, pose, and identity, providing a means to quantify the animal's behavioural dynamics and internal states at millisecond resolution. 

Further information about the project can be found in the 
[About](target-about) section.

(target-tutorials)=
## Tutorials
::::{grid} 1 2 2 2
:gutter: 3 

:::{grid-item-card} {fas}`location-crosshairs;sd-text-primary` Multi-animal tracking
:link: target-multianimal-tracking
:link-type: ref
:img-bottom: ../images/getting-started-ma.png
:img-alt:

Online tracking of multiple animals in the Aeon arena.
:::

:::{grid-item-card} {fas}`brain;sd-text-primary` Neuropixels recordings
:link: target-npx-recording
:link-type: ref
:img-bottom: ../images/getting-started-npx.png
:img-alt:

Week-long recording and analysis of Neuropixels data.
:::
::::

(target-repositories)=
## Repositories
The Aeon infrastructure is complex and multi-dimensional, spanning hardware, acquisition software, standard data formats, and a low-level API for data analysis. 
As each of these different components is built using different languages, spanning CAD programs, C# and Python, we organise Aeon into the following repositories:
::::{grid} 1 2 2 2
:gutter: 3 

:::{grid-item-card} {fas}`database;sd-text-primary` aeon_mecha
:link: https://github.com/SainsburyWellcomeCentre/aeon_mecha
:link-type: url
Aeon's main library for interfacing with acquired data
:::

:::{grid-item-card} {fas}`flask;sd-text-primary` aeon_experiments
:link: https://github.com/SainsburyWellcomeCentre/aeon_experiments
:link-type: url
Aeon experiment workflows written in the Bonsai visual programming language
:::

:::{grid-item-card} {fas}`computer;sd-text-primary` aeon_acquisition
:link: https://github.com/SainsburyWellcomeCentre/aeon_acquisition
:link-type: url
Source code for the `aeon_acquisition` Bonsai package used in 
Aeon experiment workflows
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
All experiment data is acquired and/or triggered and/or synced by 
[Harp devices](https://www.cf-hw.org/harp). 
Code in the `aeon_acquisition` and `aeon_mecha` repositories makes use of 
the [Harp protocol](harp-tech:articles/about) during data acquisition, 
raw data file writing, and raw data file reading. 
See also the documentation on 
[Harp device operation and common registers](harp-tech:protocol/Device), 
the [Harp binary protocol](harp-tech:protocol/BinaryProtocol-8bit), and 
[Harp clock synchronization](harp-tech:protocol/SynchronizationClock).
:::

:::{toctree}
:maxdepth: 1
:hidden:

installation
:::