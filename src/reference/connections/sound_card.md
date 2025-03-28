(target-wiring-sound-card)=
# Sound Card Wiring Schematic

A Harp [sound card](harp-tech:api/Harp.SoundCard) is used to deliver low latency, precisely timed audio cues, stimuli or ambient sounds or noise.
The device is connected to the behaviour machine through two separate USB connections for communication and uploading of sounds to the device's memory respectively.   

## Connections

:::{image} ../../images/sound-card-connection.svg
:alt: Sound card wiring schematic
:class: img-hardware-main
:align: center
:::

1. A micro-USB connection to the behaviour machine allows upload of prerecorded or mixed sound files to the sound card's memory. 
This is only necessary for uploading sounds and is not used for acquisition of device events.

2. A mini-USB connection to the behaviour machine is made for all other communication.

3. An RCA connection to one (for mono) or both (for stereo) ports on the sound card is made to a [Harp amplifier](https://github.com/harp-tech/peripheral.audioamp), which is then connected to the terminals of one or more speakers.

4. 12V DC power is provided to the sound card through a 2.1mm barrel jack connector from the PSU.<!--TODO Check this is correct-->

5. The sound card also receives the common clock signal from the [timestamp generator](target-wiring-timestamp-generator) via a 3.5mm audio jack connector.