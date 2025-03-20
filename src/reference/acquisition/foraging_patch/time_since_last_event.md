(target-node-timesincelastevent)=
# TimeSinceLastEvent 
The `TimeSinceLastEvent (Aeon.Foraging)` node monitors the current state of pellet delivery commands and the beam break.
<!-- TODO: Workflow file is missing
:::workflow
![Aeon.Foraging.TimeSinceLastEventWorkflow](../../../workflows/timesincelastevent.bonsai)
:::
-->
## Inputs
None

## Outputs
Sequence of `double` values carrying the number of seconds since the last event was received, accumulated from the data timestamps

## Properties
This node does not have any properties. 
However, it assumes that a `Subject` named "VideoEvents" exists and carries events from a [`CameraController`](target-node-cameracontroller) node to monitor timestamps.

## Usage
<!-- To be completed -->