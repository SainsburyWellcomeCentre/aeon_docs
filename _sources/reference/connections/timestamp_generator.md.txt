(target-wiring-timestamp-generator)=
# Timestamp Generator Wiring Schematic

A [Harp timestamp generator](harp-tech:api/Harp.TimestampGeneratorGen3.html) is used to keep all harp devices on the system synchronised and ensure they are all running on a common clock. All harp devices are connected to this timestamp generator signal via a 3.5mm stereo audio jack connection from the six `CLKout` ports on the device.

## Connections

:::{image} ../../images/timestamp-generator-connection.svg
:alt: Timestamp generator wiring schematic
:class: img-hardware-main
:align: center
:::

1. A connection to the behaviour machine is made from the mini-USB port in the device to a USB-A connection.

2. Connections to the [output expanders](target-wiring-foraging-patch-output-expander) on the foraging patches and the [camera controller](target-wiring-camera-controller) are made with a 3.5mm audio jack.

3. A connection to the Harp [sound card](target-wiring-sound-card) is also made by a 3.5mm audio jack.

4. A connection to the μHarp controller that controls the [commutation-translation system](target-wiring-commutation-translation) also recieves a 3.5mm audio jack connection.<!--TODO: this is missing in the svg -->