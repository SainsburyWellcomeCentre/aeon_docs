(target-wiring-camera-controller)=
# Camera Controller Wiring Schematic

The Harp [CameraController (Gen2)](harp-tech:api/Harp.CameraControllerGen2) device is [configured](target-module-camera-controller) to generate pulses at two different frame rates in parallel to trigger synchronised frame captures from two independent sets of cameras.

## Connections

:::{image} ../../../images/camera-controller-connection.svg
:alt: Camera controller wiring schematic
:class: img-hardware-main
:align: center
:::

The camera controller requires three connections:

1. The output trigger signals, sent to initiate frame captures on the [cameras](target-module-camera), are carried by two RJ45 cables to a breakout board, where the signal can be split to the trigger line of all cameras in the set.

2. A common clock signal is provided via a 3.5mm mini-jack connection to the [timestamp generator](target-wiring-timestamp-generator).

3. A USB connection to the behaviour machine is used to both power the device (no need for external 24V power supply) and to enable communication and data acquisition.