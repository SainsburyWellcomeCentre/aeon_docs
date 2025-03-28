# Sound card wiring schematic

A harp [sound card](https://github.com/harp-tech/device.soundcard/) is used to deliver low latency, precisely timed audio cues, stimuli or ambient sounds or noise. The device is connected to the behaviour machine through two seperate USB connections for communication and uploading of sounds to the device's memory respectively.   

## Connections

1. A micro-USB connection to the behaviour machine aloows upload of prerecorded or mixed sound files to the sound card's memory. This is only necessary for uploading sounds and is not used for acquisition of device events.

2. A mini-USB connection to the behavour machine is made for all other communication.

3. An RCA connection to one (for mono) or both (for stereo) ports on the sound card is made to a [harp amplifier](https://github.com/harp-tech/peripheral.audioamp), which it then connected to the terminals of one or more speakers.

4. 12V DC power is provided to the sound card through a 2.1mm barrel jack connector from the PSU.<!--TODO Check this is correct-->

5. The sound card also recieves the common clock signal from the timestamp generator via a 3.5mm audio jack connector.