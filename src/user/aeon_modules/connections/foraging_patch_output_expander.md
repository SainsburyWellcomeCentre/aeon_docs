(target-wiring-foraging-patch-output-expander)=
# Foraging Patch Output Expander Wiring Schematic

The [foraging patch](target-module-foraging-patch) is a motorised assembly designed to deliver dried pellets of food on a trigger, e.g. when the wheel is turned above a threshold distance, measured through a mounted [magnetic encoder](target-foraging-patch). 
This assembly is controlled by and connected to other hardware infrastructure through a [Harp output expander](harp-tech:api/Harp.OutputExpander).

## Connections

:::{image} ../../../images/foraging-patch-output-expander-connection.svg
:alt: Foraging patch output expander wiring schematic
:class: img-hardware-main
:align: center
:::

1. The output expander is connected to the behaviour machine by mini-USB, which both powers the device and enables communication between the device and computer.

2. The output expander also recieves a common clock signal through a 3.5mm stereo audio jack connection from one of the 'Clock out' ports on the [timestamp generator](target-wiring-timestamp-generator).

3. The expansion port of the output expander is connected to the magnetic encoder via a 10-pin socket (IBC10) to a 10-pin connection the magnetic encoder component of the feeder <!--TODO: I don't understand this sentence -->

4. The BNC output, 'Output0' on the output expander is connected to the 'INPUT' BNC port on the foraging patch assembly to carry the TTL pulses to deliver pellets or reset the foraging patch, determined by one of two different pulse widths.

5. The 'OUTPUT' BNC port of the foraging patch is connected to the screwgate terminals alongside the magnetic encoder socket, in order to receive the beam break events <!--TODO: URGENT: Switch output and input BNCs on .svg-->