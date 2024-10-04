:::{note}
This section is still under construction. Some information may be incomplete or unavailable at this time.
:::

(target-hardware)=
# Hardware Overview
## Main modules
:::{table}
:width: 100%
:widths: 60 40
:align: center

| Module | Files |
| --- | --- |
| **Feeder** <br>![feeder](../_static/images/hardware-overview-feeder.png){height=10em} | <ul><li>[Assembly guide](https://www.google.com)</li><li>[Bill of materials](https://www.google.com)</li></ul> |
| **Arena** <br>![arena](../_static/images/hardware-overview-arena.png){height=15em} | <ul><li>[Assembly guide](https://www.google.com)</li><li>[Bill of materials](https://www.google.com)</li></ul> |
| **Nest** <br>![nest](../_static/images/hardware-overview-nest.png){height=15em} | <ul><li>[Assembly guide](https://www.google.com)</li><li>[Bill of materials](https://www.google.com)</li></ul> |
:::

## Wiring diagrams
- [Wiring diagram 1](https://www.google.com)
- [Wiring diagram 2](https://www.google.com)

## Harp devices
| Harp Device                       | Associated Component            | Description                                                   | Quantity | 
|-----------------------------------|---------------------------------|---------------------------------------------------------------|----------|
| [**Harp Output Expander**](harp-tech:api/Harp.OutputExpander.html)                  |  Foraging Patches (Feeders)      | Expander module to connect feeder to harp system. 1 per patch | 4        |
| [**Harp CameraController Gen2**](harp-tech:api/Harp.CameraControllerGen2.html)    | Cameras                         | Controller to trigger all cameras in the arena                | 1        |
| [**Harp Timestamp Generator Gen3**](harp-tech:api/Harp.TimestampGeneratorGen3.html) | Arena (Synchronizes all devices)| Synchronizes all harp devices in the arena                    | 1        |
| [**Micropython Harp device**](https://github.com/SainsburyWellcomeCentre/microharp)       | Ephys linear rail drive         | Linear rail position controller and position sensor reciever  | 1        | 
| [**Harp SoundCard**](harp-tech:api/Harp.SoundCard.html)                  | SP speaker                      | Control and monitoring of audio speaker                     | 1        | 

<!--
:::{toctree}
:maxdepth: 1
:hidden:
hardware/feeder

::::{grid} 1 3 3 3 
:::{grid-item-card} Feeder
:img-top: ../_static/images/hardware-overview-feeder.png
:link: target-feeder
:link-type: ref
:img-bottom: ../_static/images/hardware-overview-feeder.png
:::

:::{grid-item-card} Arena
:img-bottom: ../_static/images/hardware-overview-arena.png
:::

:::{grid-item-card} Nest
:img-bottom: ../_static/images/hardware-overview-nest.png
:::
::::
-->