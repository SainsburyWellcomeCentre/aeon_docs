:::{note}
This section is still under construction. Some information may be incomplete or unavailable at this time.
:::

(target-hardware)=
# Hardware Assembly
## Main modules
| Module | Files |
| --- | --- |
| **Arena** <br>![arena](../images/hardware-overview-arena.png){height=15em align=center} | <ul><li>[Assembly guide](../downloads/Arena%20guideline%20Final%201.pdf)</li><li>[Bill of materials](../downloads/Arena%20BOM.xlsx)</li></ul> |
| **Feeder** <br>![feeder](../images/hardware-overview-feeder.png){height=12em align=center} | <ul><li>[Assembly guide](../downloads/Feeder%20Guideline%20Final%201.pdf)</li><li>[Bill of materials](../downloads/Feeder%20BOM.xlsx)</li></ul> |
| **Nest** <br>![nest](../images/hardware-overview-nest.png){height=15em align=center} | <ul><li>[Assembly guide](../downloads/Nest%20Guideline%20Final%201.pdf)</li></ul> |
| **Closed-loop translation-commutation system** <br>![linear-rail](../images/hardware-overview-linear-rail.png){height=15em align=center} | <ul><li>[Assembly guide](../downloads/Linear%20commutator%20Guideline%20Final%201.pdf)</li></ul> |

## Harp devices
| Harp Device                       | Associated Component            | Description                                                   | Quantity | 
|-----------------------------------|---------------------------------|---------------------------------------------------------------|----------|
| [**Harp Output Expander**](harp-tech:api/Harp.OutputExpander.html)                  |  Foraging Patches (Feeders)      | Expander module to connect feeder to harp system. 1 per patch | 4        |
| [**Harp CameraController Gen2**](harp-tech:api/Harp.CameraControllerGen2.html)    | Cameras                         | Controller to trigger all cameras in the arena                | 1        |
| [**Harp Timestamp Generator Gen3**](harp-tech:api/Harp.TimestampGeneratorGen3.html) | Arena (Synchronizes all devices)| Synchronizes all harp devices in the arena                    | 1        |
| [**Micropython Harp device**](https://github.com/SainsburyWellcomeCentre/microharp)       | Ephys linear rail drive         | Linear rail position controller and position sensor reciever  | 1        | 
| [**Harp SoundCard**](harp-tech:api/Harp.SoundCard.html)                  | SP speaker                      | Control and monitoring of audio speaker                     | 1        | 

## Wiring diagrams
- [Wiring diagram](../downloads/Example%20wiring%20diagram.pdf)

<!--
:::{toctree}
:maxdepth: 1
:hidden:
hardware/feeder

::::{grid} 1 3 3 3 
:::{grid-item-card} Feeder
:img-top: ../images/hardware-overview-feeder.png
:link: target-feeder
:link-type: ref
:img-bottom: ../images/hardware-overview-feeder.png
:::

:::{grid-item-card} Arena
:img-bottom: ../images/hardware-overview-arena.png
:::

:::{grid-item-card} Nest
:img-bottom: ../images/hardware-overview-nest.png
:::
::::
-->