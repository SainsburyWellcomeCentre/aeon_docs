# Timestamp generator wiring schematic

A [harp timestamp generator](https://github.com/harp-tech/device.timestampgeneratorgen3) is used to keep all harp devices on the system synchronised and ensure they are all running on a common clock. All harp devices are connected to this timestamp generator signal via a 3.5mm stereo audio jack connection from the six `CLKout` ports on the device.

## Connections

1. A connection to the behaviour machine is made from the mini-USB port in the device to a USB-A connection.

2. Connections to the [output expanders](./output_expander_feeder.md) on the feeders, the [camera controller](./camera_controller.md) are made with a 3.5mm audio jack.

3. A connection to the harp [soundcard](./sound_card.md) is also made by a 3.5mm audio jack.

4. A connection to the μHarp controller that controls the [linear commutator](./linear_commutator.md) also recieves a 3.5mm audio jack connection.<!--TODO: this is missing in the svg -->