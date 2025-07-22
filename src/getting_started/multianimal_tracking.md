(target-multianimal-tracking)=
# Multi-Animal Tracking

:::{figure} ../images/ma-main.png
:alt: multi-animal-tracking
:class: img-getting-started-large
:width: 60%

Online tracking of location, poses and identity of individual animals allows for quantification of natural behaviours.
:::
By quantifying position and locomotion speed as well as estimating the poses of multiple animals over weeks, we can identify the emergence of spontaneous behaviours such as foraging, as well as investigate social dynamics and individual strategies and their modulation by environmental influences. 
This is possible through the multipronged approach using the computer vision software [SLEAP](sleap:) on multiple cameras and RFID sensors embedded in a single [experimental workflow](target-general-experimental-workflow).

## Identity model
:::{image} ../images/ma-identity-model.png
:alt: sleap-id-model
:class: img-getting-started-small
:align: center
:::

To enable reliable individual identification, distinctive band patterns are tattooed on the mice's tails as clear and stable markers.
Four overhead quadrant cameras capture high-resolution, zoomed-in views of the [habitat](target-habitat), allowing the experiment-specific SLEAP identity model to track each mouse based on its unique tail pattern.
These identity models are trained for each unique set of subjects.

*Relevant repositories: [aeon_sleap_processing](aeon-sleap-processing-github:)*

## Pose model
:::{image} ../images/ma-pose-model.png
:alt: sleap-pose-model
:class: img-getting-started-small
:align: center
:::

The SLEAP pose model tracks eight body parts along each mouse using an overhead camera that captures the entire habitat. 
Unlike identity models, the pose model is designed to be reusable across experiments with similar setups.

*Relevant repositories: [aeon_sleap_processing](aeon-sleap-processing-github:)*

## Inference pipeline
:::{image} ../images/ma-inference-pipeline.png
:alt: multi-animal-tracking
:class: img-getting-started-large
:align: center
:::

The identity model processes all quadrant views, assigning an identity and a likelihood score to each detected mouse. 
For each mouse, the prediction with the highest likelihood is selected and projected onto the full-field camera view. 
The pose model then estimates the pose of each mouse in the full-field view.
The final output combines both pose and identity assignments.

*Relevant repositories: [aeon_sleap_processing](aeon-sleap-processing-github:)*

## RFID validation
Each mouse is implanted with an RFID tag, enabling automatic detection of its presence at key locations within the habitat which are equipped with RFID antennae ([nest](target-nest), [foraging patches](target-foraging-patch), gates).
These RFID detections provide ground-truth data for validating the accuracy of identity tracking.

*Relevant repositories: [aeon_sleap_processing](aeon-sleap-processing-github:)*
