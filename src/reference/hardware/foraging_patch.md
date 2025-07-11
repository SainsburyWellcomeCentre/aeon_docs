(target-foraging-patch)=
# Foraging Patch
:::{image} ../../images/foraging-patch.svg
:alt: Foraging Patch
:class: img-hardware-main
:align: center
:::

The foraging patch, consisting of the foraging wheel and the pellet delivery system, is utilised with the [foraging patch acquisition module](target-module-foraging-patch) to provide a means for animals to obtain food in the [habitat](target-habitat) by rotating the wheel, simulating a naturalistic digging action. 

The foraging wheel features two sets of pockets on its surface:  "grip pockets" that allow the animal to grasp and rotate the wheel, and "pellet pockets" designed to collect food pellets. 
The wheel's pivot is supported by ball bearings for unidirectional rotation and a magnetic encoder measures the wheel's movement. 
Pellets are stored in an underground hopper and are dispensed onto the wheel via a motor-driven spinning disk. 
An infrared beam-break sensor detects the pellets as they are delivered.

_Dimensions: L = 190mm, W = 168mm, H = 83mm_

## Parts list
:::{image} ../../images/foraging-patch-partlist.svg
:alt: Parts
:align: center
:::

## Assembly guide
### Pellet hopper
::::{dropdown} Steps 1-5
:::{figure} ../../images/foraging-patch-step1.svg
:alt: step1
:class: img-hardware-steps
:figclass: caption-hardware-steps
1\. Create a flat surface on the motor shaft by filing it or using a handheld dremel.
:::
:::{figure} ../../images/foraging-patch-step2.svg
:alt: step2
:class: img-hardware-steps
:figclass: caption-hardware-steps
2\. Rotate the foraging patch base and insert the motor. Screw the motor in place from the front using three screws (ID 2).
:::
:::{figure} ../../images/foraging-patch-step3.svg
:alt: step3
:class: img-hardware-steps
:figclass: caption-hardware-steps
3\. Carefully handle the track and gently insert it in the foraging patch making sure of aligning the holes. Rotate the foraging patch base and hold the track in place by using six screws (ID 5).
:::
:::{figure} ../../images/foraging-patch-step4.svg
:alt: step4
:class: img-hardware-steps
:figclass: caption-hardware-steps
4\. Lower the disk into the foraging patch base making sure to orient the grub screw tapped hole toward the flat surface previously created on the motor metal pin (see step 1). Push down the disk until the top of the pin is flush to the disk itself and use a grub screw (ID 10) to hold the disk in place. Make sure the grub screw touches the flat surface of the trimmed motor pin.
:::
:::{figure} ../../images/foraging-patch-step5.svg
:alt: step5
:class: img-hardware-steps
:figclass: caption-hardware-steps
5\. Insert two short silicon tubes in each pellet stopper pin and screw it in place with two screws (ID 4).
:::
::::

### Infrared sensor
::::{dropdown} Steps 6-8 
:::{figure} ../../images/foraging-patch-step6.svg
:alt: step6
:class: img-hardware-steps
:figclass: caption-hardware-steps
6\. Place the wheel frame on the foraging patch base with 4 screws (ID 4).
:::
:::{figure} ../../images/foraging-patch-step7.svg
:alt: step7
:class: img-hardware-steps
:figclass: caption-hardware-steps
7\. Carefully insert the beam break PCB board into the beam break holder (ID 12).
:::
:::{figure} ../../images/foraging-patch-step8.svg
:alt: step8
:class: img-hardware-steps
:figclass: caption-hardware-steps
8\. Slot the beam break holder in the back of the foraging patch base and screw it in place from the front (ID 1).
:::
::::

### Wheel assembly
::::{dropdown} Steps 9-14 
:::{figure} ../../images/foraging-patch-step9.svg
:alt: step9
:class: img-hardware-steps
:figclass: caption-hardware-steps
9\. Hold the wheel holder base on the back of the foraging patch base and screw it in place with 3 screws (ID 11, see colours).
:::
:::{figure} ../../images/foraging-patch-step10.svg
:alt: step10
:class: img-hardware-steps
:figclass: caption-hardware-steps
10\. Insert two parallel pin (ID 13) in the middle holes. If needed, enlarge the holes using a reamer.
:::
:::{figure} ../../images/foraging-patch-step11.svg
:alt: step11
:class: img-hardware-steps
:figclass: caption-hardware-steps
11\. Slide the one-way bearing, the spacer and the two-way bearing onto the bolt.
:::
:::{figure} ../../images/foraging-patch-step12.svg
:alt: step12
:class: img-hardware-steps
:figclass: caption-hardware-steps
12\. Insert the shoulder bolt into the wheel hole and tighten it in place using a lock nut. If needed, enlarge the hole using a reamer. Holding the shoulder bolt, insert the magnet holder on the cap and put the neodymium magnet into place (the magnet will hold its position).
:::
:::{figure} ../../images/foraging-patch-step13.svg
:alt: step13
:class: img-hardware-steps
:figclass: caption-hardware-steps
13\. Rotate the foraging patch on its back and place the shoulder bolt with the bearings onto the wheel holder base. The wheel should sit within the foraging patch base opening (blue).
:::
:::{figure} ../../images/foraging-patch-step14.svg
:alt: step14
:class: img-hardware-steps
:figclass: caption-hardware-steps
14\. Lower the wheel holder top onto the bearing and insert the pins. Carefully align the holder base and top using the pins as well as 4 screws (ID 9).The aim is to obtain an equally spaced gap between the wheel holder base and the top.
:::
::::

### Magnetic encoder
::::{dropdown} Steps 15-16
:::{figure} ../../images/foraging-patch-step15.svg
:alt: step15
:class: img-hardware-steps
:figclass: caption-hardware-steps
15\. Screw the magnetic encoder holder into place (ID 1).
:::
:::{figure} ../../images/foraging-patch-step16.svg
:alt: step16
:class: img-hardware-steps
:figclass: caption-hardware-steps
16\. Gently place the magnetic encoder onto its holder (ID 7). The magnet should face the magnetic encoder chip.
:::
::::

### Electronics
::::{dropdown} Steps 17-19
:::{figure} ../../images/foraging-patch-step17.svg
:alt: step17
:class: img-hardware-steps
:figclass: caption-hardware-steps
17\. Screw the electronic box on the side of the foraging patch base (ID 6) and insert the foraging patch electronics. The screws need to be inserted from the inside of the box itself.
:::
:::{figure} ../../images/foraging-patch-step18.svg
:alt: step18
:class: img-hardware-steps
:figclass: caption-hardware-steps
18\. Add the Raspberry Pi Pico to the foraging patch electronics.
:::
:::{figure} ../../images/foraging-patch-step19.svg
:alt: step19
:class: img-hardware-steps
:figclass: caption-hardware-steps
19\. Close the box with the electronic box lid (ID 8).
:::
::::

### Foraging patch tile
::::{dropdown} Steps 20-21
:::{figure} ../../images/foraging-patch-step20.svg
:alt: step20
:class: img-hardware-steps
:figclass: caption-hardware-steps
20\. Attach the assembled foraging patch to the metal hexagon tile using 6 screws (ID 3). Note: make a 1.25mm thick and 18mm wide rim all around the bottom of the metal hex tile using a milling machine.
:::
:::{figure} ../../images/foraging-patch-step21.svg
:alt: step21
:class: img-hardware-steps
:figclass: caption-hardware-steps
21\. To complete the foraging patch, add the tile orienting the tile engraving with the foraging patch. Metal tile and foraging patch tile should be flush and only the wheel exposed.
:::
::::

## Downloads
- [Assembly guide](../../downloads/Foraging-Patch-Guideline.pdf)
- [Bill of materials](../../downloads/Foraging-Patch-BOM.xlsx)