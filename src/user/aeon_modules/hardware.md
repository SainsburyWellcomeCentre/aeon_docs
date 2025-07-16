:::{note}
This section is still under construction. Some information may be incomplete or unavailable at this time.
:::

(target-hardware)=
# Hardware Assembly
The Aeon system consists of a modular, scalable, and programmable habitat equipped with various interactive and non-interactive modules, such as [foraging patches](target-foraging-patch) and [nests](target-nest). 
Here, you will find comprehensive guidelines and parts lists to help you replicate the main modules or inspire you to create your own. 

## Main modules
::::{grid} 1 2 2 2
:gutter: 1

:::{grid-item-card} Commutation-translation system
:link: target-commutation-translation
:link-type: ref
:img-bottom: ../../images/commutation-translation-system.svg
:class-card: module-card
:::

:::{grid-item-card} Foraging Patch
:link: target-foraging-patch
:link-type: ref
:img-bottom: ../../images/foraging-patch.svg
:class-card: module-card
:::

:::{grid-item-card} Habitat
:link: target-habitat
:link-type: ref
:img-bottom: ../../images/habitat.svg
:class-card: module-card
:::

:::{grid-item-card} Nest
:link: target-nest
:link-type: ref
:img-bottom: ../../images/nest.svg
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

## Wiring schematics
<!-- - [Wiring diagram](../downloads/Example-Wiring-Diagram.pdf) Do we still want this?-->
- [Camera](target-wiring-camera)
- [Camera controller](target-wiring-camera-controller)
- [Commutation-translation system](target-wiring-commutation-translation)
- [Foraging patch](target-wiring-foraging-patch)
- [Foraging patch output expander](target-wiring-foraging-patch-output-expander)
- [Microphone](target-wiring-microphone)
- [RFID Reader](target-wiring-rfid-reader)
- [Sound card](target-wiring-sound-card)
- [Timestamp generator](target-wiring-timestamp-generator)
- [Weighing scale](target-wiring-weighing-scale)


:::{toctree}
:maxdepth: 1
:hidden:
:glob:

hardware/*
connections/*
:::