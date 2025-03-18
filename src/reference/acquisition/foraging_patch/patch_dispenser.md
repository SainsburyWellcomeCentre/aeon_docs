(target-node-patchdispenser)=
# PatchDispenser
The `PatchDispenser (Aeon.Foraging)` node keeps track of the number of pellets available to the feeder, generating events for each dispensed pellet, detailing the number of remaining pellets and the reason a pellet was dispensed. 
Additionally, it constructs [a visualiser and a control panel](target-node-patchdispenser-control-panel) for controlling the basic and manual functions of the feeder.
This node accepts pellet discount notifications triggered by the IR beam break following each successful pellet delivery, and discounts these from the total number of remaining pellets, which is itself set manually in the [control panel](target-module-control-panel) when loading the feeder hopper. 
The state of the dispenser is stored in a `StateRecoverySubject` to retain the feeder's status in the event of a breakdown that requires restarting the workflow.

## Inputs
`Harp.Timestamped<bool>` events emitted by the [`UndergroundFeeder`](target-node-undergroundfeeder) node indicating pellet delivery. 

## Outputs
Stream of custom class `Aeon.Foraging.DispenserEventArgs`. 
Each item emitted consists of a "Value" (`int`) corresponding to the pellet count following an event, and an "EventType" (`Aeon.Foraging.DispenserEventType`) describing the reason for the new pellet count, i.e. due to a triggered "Discount", or "Reset" or "Refill" command from the [control panel](target-module-control-panel).

## Properties
### General
| Property name | Description                                               |
|---------------|-----------------------------------------------------------|
| **Name**      | Set the name to identify this specific dispenser module. e.g. "Patch1" |

### Subjects
Events (outputs) from the `PatchDispenser` node are published to shared `Subject`s, the names of which are configured in the properties of the node. 
These subjects then become accessible in the Bonsai editor's toolbox for use elsewhere for logging and visualisation.

#### Device event subjects
| Subject name      | Property Type | Expected Data Type       | Description                   |
|-------------------|-------------|-------------------------|----------------------------------|
| **ControllerEvents** | `string` | `Aeon.Foraging.DispenserEventArgs` | Controller events shared `Subject`, carrying the number of remaining pellets (`int`) and the `EventType`. Also output directly by the node |
| **DispenserState** | `string` | `Tuple<double,double,double>`  | Declared `StateRecoverySubject` to store the current `Threshold`, `D1`, and `Delta` parameters of the pellet dispenser |

## Usage
Place a `SubscribeSubject` and set the name property to the "PelletDelivered" `Subject` for a patch (e.g. "Patch1PelletDelivered"). 
Connect this to a `Condition` node that checks the `Value` of the incoming `Subject`. 
This is a `Boolean` that reports `True` on pellet delivery, and ensures only the rising edge of this signal is counted as a delivery. 
Place and configure the properties of a `PatchDispenser` node, setting the names of the output `Subject`s.

:::workflow
![Aeon.Foraging.PatchDispenser](../../../workflows/patchDispenser.bonsai)
:::