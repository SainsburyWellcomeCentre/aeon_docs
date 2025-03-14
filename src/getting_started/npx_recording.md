(target-npx-recording)=
# Neuropixels Recordings

:::{figure} ../images/npx-main.png
:height: 300px
:alt: neuropixels-recording

Week-long continuous neural recordings from a freely moving animal in a large environment.
:::

Conducting continuous neural recordings over multiple days in a large environment presents several technical challenges. 
It is crucial to ensure that the animal's movement is unrestricted and that the recording quality remains stable over time. To achieve this, it is essential to:

1. Maintain a constant slack in the recording tether, regardless of the mouse's location in the habitat.
2. Prevent the tether from tangling when the mouse turns.

To address these challenges, we developed a [closed-loop control system](target-commutation-translation) capable of untwisting the cable using the [ONIX torque-free commutator](https://open-ephys.org/commutator-info) and translating it based on the mouse's position.

## Closed-loop control of commutator location
::::{grid} 2
:margin: 0

:::{grid-item}
:columns: 4
:child-align: center
![commutator-location-control](../images/npx-commutator-location.png)
:::
:::{grid-item}
:columns: 8
:child-align: center

Using the live position estimate from the overhead camera, we can control the horizontal position of the commutator on a linear rail to follow the animal as it moves through the habitat. 

*Relevant repositories: [aeon_experiments](aeon-experiments-github:), [aeon_lineardrive](aeon-lineardrive-github:)*
:::
::::

## Closed-loop control of commutator rotation
::::{grid} 2
:margin: 0

:::{grid-item}
:columns: 4
:child-align: center
![commutator-rotation-control](../images/npx-commutator-rotation.png)
:::
:::{grid-item}
:columns: 8
:child-align: center

Using the heading direction computed by the IMU sensor on the [ONIX neuropixels headstage](https://open-ephys.github.io/onix-docs/Hardware%20Guide/Headstages/headstage-neuropix-2e-beta.html), the cable commutation is adapted in real time to avoid tangling.

*Relevant repositories: [aeon_experiments](aeon-experiments-github:), [bonsai-commutator](https://github.com/open-ephys/bonsai-commutator), [bonsai-onix1](https://github.com/open-ephys/bonsai-onix1)*
:::
::::

## Neuropixels 2.0 recordings
::::{grid} 2
:margin: 0

:::{grid-item}
:columns: 4
:child-align: center
![npx-20-recordings](../images/npx-recording-sites.png)
:::
:::{grid-item}
:columns: 8
:child-align: center

All data are acquired using the [ONIX recording system](https://open-ephys.github.io/onix-docs/index.html), which supports simultaneous recording with two [Neuropixels 2.0 probes](https://www.neuropixels.org/probe2-0). 

*Relevant repositories: [bonsai-onix1](https://github.com/open-ephys/bonsai-onix1)*
:::
::::
