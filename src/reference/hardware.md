:::{note}
This section is still under construction. Some information may be incomplete or unavailable at this time.
:::

(target-hardware)=
# Hardware Overview
The Aeon system consists of a modular, scalable, and programmable habitat equipped with various interactive and non-interactive modules, such as [foraging patches](target-foraging-patch) and [nests](target-nest). 
Here, you will find comprehensive guidelines and parts lists to help you replicate the main modules or inspire you to create your own. 

## Main modules
::::{grid} 1 3 3 3
:gutter: 1

:::{grid-item-card} Commutation-translation system
:link: target-commutation-translation
:link-type: ref
:img-bottom: ../images/hardware-overview-linear-commutator.png
:class-card: module-card
:::

:::{grid-item-card} Foraging Patch
:link: target-foraging-patch
:link-type: ref
:img-bottom: ../images/hardware-overview-foraging-patch.png
:class-card: module-card
:::

:::{grid-item-card} Habitat
:link: target-habitat
:link-type: ref
:img-bottom: ../images/hardware-overview-habitat.png
:class-card: module-card
:::

:::{grid-item-card} Nest
:link: target-nest
:link-type: ref
:img-bottom: ../images/hardware-overview-nest.png
:class-card: module-card
:::
::::

## Harp devices
| Harp Device                       | Associated Component            | Description                                                   | Quantity | 
|-----------------------------------|---------------------------------|---------------------------------------------------------------|----------|
| [**Harp Output Expander**](harp-tech:api/Harp.OutputExpander.html)                  |  Foraging Patches (Feeders)      | Expander module to connect foraging patch to Harp system. 1 per patch | 4        |
| [**Harp CameraController Gen2**](harp-tech:api/Harp.CameraControllerGen2.html)    | Cameras                         | Controller to trigger all cameras in the habitat                | 1        |
| [**Harp Timestamp Generator Gen3**](harp-tech:api/Harp.TimestampGeneratorGen3.html) | Habitat (Synchronises all devices)| Synchronises all Harp devices in the habitat                    | 1        |
| [**Micropython Harp device**](https://github.com/SainsburyWellcomeCentre/microharp)       | Ephys linear rail drive         | Linear rail position controller and position sensor reciever  | 1        | 
| [**Harp SoundCard**](harp-tech:api/Harp.SoundCard.html)                  | SP speaker                      | Control and monitoring of audio speaker                     | 1        | 

## Wiring diagrams
- [Wiring diagram](../downloads/Example-Wiring-Diagram.pdf)

:::{toctree}
:maxdepth: 1
:hidden:
:glob:

hardware/*
:::