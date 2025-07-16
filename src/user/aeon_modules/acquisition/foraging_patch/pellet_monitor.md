(target-node-pelletmonitor)=
# PelletMonitor 
The `PelletMonitor (Aeon.Foraging)` node monitors the current state of pellet delivery commands and the beam break.
Within this node, pellet delivery commands received by the [Harp output expander](harp-tech:api/Harp.OutputExpander) are filtered from the "PatchEvents" `Subject` and successful deliveries monitored through the "PelletDelivered" `Subject` (e.g. "Patch1PelletDelivered"). 
The `RepeatEverySubject` node ensures this node is only running while an animal is present in the habitat. <!-- This is not that clear to me; it seems to only run when a subject has entered, but if you had two subjects and removed one this would it not also stop, despite there being another subject stil present? -->

:::workflow
![Aeon.Foraging.PelletMonitorWorkflow](../../../../workflows/pelletMonitorWorkflow.bonsai)
:::

## Inputs
None

## Outputs
Sequence of dynamic class events triggered by deliver pellet commands and beam break events, consisting of a "Timestamp" (`double`) and a "Value" (`boolean`) that reports the current state. 
This "Value" is `True` if and when a delivery command has been received, and `False` when a successful beam break is detected. 

## Properties
### Subjects
Inputs to the `PelletMonitor` node are subscribed to from shared `Subject`s, the names of which are configured in the properties of the node. 

#### Device input subjects
| Subject name      | Property Type        | Expected Data Type | Description                   |
|-------------------|----------------------|--------------------|------------------------------|
| **PelletCommand** | `string` | `Harp.HarpMessage`  | The name of the shared `Subject` carrying all events published by the [output expander](harp-tech:api/Harp.OutputExpander) connected to an [`UndergroundFeeder`](target-node-undergroundfeeder), e.g. "Patch1Events" |
| **PelletDelivered**| `string` | `Harp.Timestamped<bool>` | The name of the shared `Subject` carrying beam break events indicating successful pellet deliveries, e.g. "Patch1PelletDelivered". Also published by [`UndergroundFeeder`](target-node-undergroundfeeder) |

## Usage
To use a `PelletMonitor (Aeon.Foraging)` node, simply place one and configure its properties. 

:::workflow
![Aeon.Foraging.PelletMonitor](../../../../workflows/pelletMonitor.bonsai)
:::