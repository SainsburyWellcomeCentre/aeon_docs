# Foraging patch wiring schematic

A <!--TODO-->[foraging patch](./link/to/acquisition/foraging_patch.md) is a motorised assembly designed to deliver dried pellets of food on a trigger. For example, when the wheel is turned above a threshold distance, measured through a mounted magnetic encoder (see <!--TODO-->[feeder assembly](./link/to/feeder_hardware.md)). This assembly is controlled by and connected to other hardware infrastructure through a harp [output expander](https://github.com/harp-tech/device.outputexpander).

## Connections
1. The output expander is connected to the behaviour machine by mini-USB, which both powers the device and enables communication between the device and computer.

2. The output expander also recieves a common clock signal through a 3.5mm stereo audio jack connection from one of the 'Clock out' ports on the [timestamp_generator](./timestamp_generator.md).

3. The expansion port of the output expander is connected to the magnetic encoder via a 10-pin socket (IBC10) to a 10-pin connection the magnetic encoder component of the feeder.

4. The BNC output, 'Output0' on the output expander is connected to the 'INPUT' BNC port on the feeder assembly to carry the TTL pulses to deliver pellets or reset the feeder, determined by one of two different pulse widths.

5. The 'OUTPUT' BNC port of the feeder is connected to the screwgate terminals alongside the magnetic encoder socket, in order to receive the beam break events <!--TODO: URGENT: Switch output and input BNCs on .svg-->