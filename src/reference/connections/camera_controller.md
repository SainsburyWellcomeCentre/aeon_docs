# Harp camera controller wiring schematic

The [camera controller](./camera_controller.md) Harp device is configured to generate pulses at two different frame rates in parallel to trigger synchronised frame captures from two independent sets of cameras.

## Connections
The camera controller requires three connections: the output trigger signals sent to trigger frame captures on the cameras; the synchronizing clock signal; power; and communication with the behaviour machine.

1. The trigger signals are carried by two RJ45 cables to a breakout board, where the signal can be split to the trigger line of all cameras in the set (see [camera wiring diagram](./Camera.svg))

2. A common clock signal via a 3.5mm mini-jack connection to the [timestamp generator](./Timestamp_generator.svg)

3. A USB connection to the behaviour machine is used to both power the device  (no need for external 24V power supply) and for communication and acquisition.