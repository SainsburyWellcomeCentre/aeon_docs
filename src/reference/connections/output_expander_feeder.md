# Foraging patch wiring schematic

A <!--TODO-->[foraging patch](./link/to/acquisition/foraging_patch.md) is a motorised assembly designed to deliver dried pellets of food on a trigger. For example, when the wheel is turned above a threshold distance, measured through a mounted magnetic encoder (see <!--TODO-->[feeder assembly](./link/to/feeder_hardware.md)). This assembly is controlled by and connected to other hardware infrastructure through a harp [output expander](https://github.com/harp-tech/device.outputexpander).

## Connections
1. The output expander is connected to the behaviour machine by mini-USB, which both powers the device and enables communication between the device and computer.

2. The output expander also recieves a common clock signal through a 3.5mm audio jack connection from one of the 'Clock out' ports on the [timestamp_generator](./timestamp_generator.md).

3. In order to connect and control the behaviour of the <!--TODO-->[feeder assembly](./link/to/feeder_hardware.md), the serial expansion port of the output expander connects to the feeder assembly via a 10-pin COM port (IBC10) direct to a 9-pin serial connection (DB9) on the feeder assembly. Pin 10 is not used. <!--TODO: URGENT: Check if the pinout is needed here-->

4. The BNC output, 'Output0' on the output expander is connected to the 'INPUT' BNC port on the feeder.

5. The 'OUTPUT' BNC port of the feeder is connected to the pellet detecting IR beam break, and connected to the screwgate terminals of the feeder socket. <!--TODO: URGENT: Check I haven't gotten this mixed up, or if the svg is mixed up-->