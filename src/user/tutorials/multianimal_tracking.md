(target-multianimal-tracking)=
# Multi-animal tracking

:::{figure} ../../_static/images/getting-started-ma.png
:height: 300px
:alt: multi-animal-tracking

Online tracking of location and identity of individual animals allows for quantification of natural behaviours.
:::
By quantifying both position as well as locomotion speed of multiple animals over weeks, we can identify the emergence of spontaneous behaviours such as foraging, as well as investigate social dynamics and individual strategies and their modulation by environmental influences.
This is possible through the multipronged approach using multiple cameras as well as RFID sensors embedded in a single workflow.

## Live position tracking
![live-position-tracking](../../_static/images/ma-live-position-tracking.png){width=250px align=left}
An overhead camera with a view of the entire arena feeds into a Bonsai workflow and
continuously estimates the animals' x, y positions, body length, and orientation.

*Relevant repositories: [aeon_experiment](aeon-experiments-github:), [aeon_acquisition](aeon-acquisition-github:)*

## Identifying animals
![identifying-animals](../../_static/images/ma-identifying-animals.png){width=250px align=left}
When there are multiple animals in the arena, identity of each animal can be
determined using computer vision ([SLEAP](https://sleap.ai/)) from the overhead camera using the individual tail tattoos (one
band, two bands, or none) as features. Furthermore, animals are implanted with RFID tags that
allow us to quantify their visits to important sites (nest, foraging patches, gates) which are equipped with RFID antennae. 

*Relevant repositories: [aeon_experiment](aeon-experiments-github:), [aeon_acquisition](aeon-acquisition-github:)*

## Pose estimation
![pose-estimation](../../_static/images/ma-pose-estimation.png){width=250px align=left}
A zoomed-in view of the overhead camera together with side-view cameras at
behavioural hotspots such as the foraging patches allows for analysis of posture.

*Relevant repositories: [aeon_experiment](aeon-experiments-github:), [aeon_acquisition](aeon-acquisition-github:)*
