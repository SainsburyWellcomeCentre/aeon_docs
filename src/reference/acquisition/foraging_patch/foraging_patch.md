(target-module-foraging-patch)=
# Foraging Patch

The foraging patch module is core to foraging and long-term 24/7 experiments. 
It is utilised with a [feeder](target-feeder) hardware module assembly to provide a means for animals in the arena to obtain food by turning a configurable wheel, simulating a naturalistic digging action. 

The primary [`UndergroundFeeder (Aeon.Foraging)`](#undergroundfeeder) node handles the connection to the feeder hardware through a [Harp output expander](https://github.com/harp-tech/device.outputexpander) and defines the basic functions of the feeder.

To extend the functionality of the feeder, the following auxiliary nodes are provided:
- [`PatchDispenser (Aeon.Foraging)`](#patchdispenser)
- [`PelletMonitor (Aeon.Foraging)`](#pelletmonitor)
- [`TimeSpentOnWheel (Aeon.Foraging)`](#timespentonwheel)
- [`TimeSinceLastEvent (Aeon.Foraging)`](#timesincelastevent)

Each of these auxiliary nodes accept events carried by shared `Subject`s from the `UndergroundFeeder` node. These together create a comprehensive foraging assembly known as a "Patch" that allows for real-time tracking of various measures extracted from processing sensor data and events from the feeder device, including:
- PelletCount
- TimeSpentOnPatches
- TimeSinceLastVisit
- TotalDistanceTravelled
- MissedPellets
- ManualPellets
- TotalPelletsDelivered

## Nodes
### UndergroundFeeder
The `UndergroundFeeder (Aeon.Foraging)` node establishes a connection to the [feeder](target-feeder) hardware module assembly through a [Harp output expander](https://github.com/harp-tech/device.outputexpander). 
It also defines the basic functions of the feeder and a workflow to configure the relevant device operation properties. 
The device uses the standardised Harp communication protocol, producing timestamped Harp messages when device events occur.

#### Inputs
None

#### Outputs
Stream of all `Harp.HarpMessages` emitted by the Harp device.

#### Properties
##### General
These properties are critical parameters for the operation of the device.

| Property name | Description                                               |
|---------------|-----------------------------------------------------------|
| **PortName**  | The COM port the output expander attached to your feeder is connected to |
| **Radius**    | The radius of the foraging wheel in centimeters. This is used to compute the distance the wheel has been turned. The Aeon [foraging patch](target-feeder) wheel has a radius of 4cm |
| **SampleRate**| The sampling rate of the magnetic encoder monitoring the wheel, selected from options available. For Aeon experiments, this is set to 500Hz |

##### Retry function
If a pellet is due to be delivered, an IR beam break module in the feeder detects whether the pellet delivery is successful. 
In the event that a pellet is not delivered (no beam break detected), then the feeder can be configured to try again. 
These properties configure the options around this functionality.

| Property name | Description                                   |
|---------------|-----------------------------------------------|
| **DueTime**   | The time following a pellet delivery command that the device will wait for a successful beam break signal before assuming the pellet delivery has failed |
| **Count**     | The number of retry attempts the feeder will perform |

##### Subjects
Events (outputs) from and commands (inputs) to the feeder node are published to shared `Subject`s, the names of which are configured in the properties of the node. 
The output `Subject`s are then accessible in the Bonsai editor's toolbox and are useable elsewhere in the workflow using the same names.

###### Device event subjects
| Subject name      | Type        | Description                   |
|-------------------|-------------|-------------------------------|
| **PatchEvents**      | `Harp.HarpMessage`       | Contains all events, consisting of timestamped Harp messages reporting the state of each register of the output expander. Also output directly by the `UndergroundFeeder` node |
| **WheelDisplacement**| `Harp.Timestamped<double>`| The sample-to-sample displacement of the foraging wheel in mm           |
| **PelletDelivered**  | `Harp.Timestamped<bool>`  | Reports `True` when a pellet is detected by the IR beam break register |

###### Device command subjects
| Subject name      | Type          | Description                                                                                     |
|-------------------|---------------|-------------------------------------------------------------------------------------------------|
| **DeliverPellet**    | `object`   | Trigger pellet delivery. Any event passed to this `Subject` will trigger a pellet delivery      |
| **ResetFeeder**      | `object`   | Trigger feeder reset. Any event passed to this `Subject` will trigger a feeder reset |

#### Usage
Create a `GroupWorkflow` and give it an appropriate name, e.g. "Patch1". 
Inside, place an `UndergroundFeeder (Aeon.Foraging)` node, externalise all properties, and connect it to the `WorkflowOutput`:

:::workflow
![Aeon.Foraging.UndergroundFeeder](../../workflows/base-feeder.bonsai)
:::

### PatchDispenser 
The `PatchDispenser (Aeon.Foraging)` node keeps track of the number of pellets available to the feeder. 
It accepts pellet discount notifications triggered by the IR beam break following successful pellet delivery, and discounts these from the total number of pellets, which is itself set manually when loading the feeder hopper.

#### Inputs
`Harp.Timestamped<bool>` events emitted by the `UndergroundFeeder` node indicating pellet delivery. 

#### Outputs
Stream of custom class `Aeon.Foraging.DispenserEventArgs`. 
<!-- TODO: Fix link to controlpanel -->
Each item emitted consists of a "Value" (`int`) corresponding to the pellet count following an event, and an "EventType" (`Aeon.Foraging.DispenserEventType`) describing the reason for the new pellet count, i.e. due to a triggered "Discount", or "Reset" or "Refill" command from the [control panel](../../GUI/controlPanel.md).

#### Properties
##### General
| Property name | Description                                               |
|---------------|-----------------------------------------------------------|
| **Name**      | Set the name to identify this specific dispenser module. e.g. "Patch1" |

##### Subjects
Events (outputs) from the `PatchDispenser` node are published to shared `Subject`s, the names of which are configured in the properties of the node. 
These subjects then become accessible in the Bonsai editor's toolbox for use elsewhere under the same name

###### Device event subjects
| Subject name      | Type        | Description                   |
|-------------------|-------------|-------------------------------|
| **ControllerEvents** | `Aeon.Foraging.DispenserEventArgs` | Controller events shared `Subject`, carrying the number of pellets remaining (`int`) and the `EventType`. Also output directly by the node |
| **DispenserState** | `Tuple<double,double,double>`  | Declared `StateRecoverySubject` to store the current Threshold, D1, and Delta parameters of the pellet dispenser |

#### Usage
Place a `SubscribeSubject` and point it to the "PelletDelivered" `Subject` for a patch (e.g. "Patch1PelletDelivered"). 
Connect this to a `Condition` node that checks the `Value` of the incoming `Subject`. 
This is a `Boolean` that reports `True` on pellet delivery, and ensures only the rising edge of this signal is counted as a delivery. 
Finally, connect this to a `PatchDispenser (Aeon.Foraging)` node.

:::workflow
![Aeon.Foraging.PatchDispenser](../../workflows/patchDispenser.bonsai)
:::

### PelletMonitor 
The `PelletMonitor (Aeon.Foraging)` node monitors the current state of pellet delivery commands and the beam break.
Within this node, pellet delivery commands received by the Harp output expander are filtered from the "PatchEvents" `Subject` and successful deliveries monitored through the "PelletDelivered" `Subject` (e.g. "Patch1PelletDelivered"). 
The `RepeatEverySubject` node ensures this node is only running while an animal is present in the arena. <!-- This is not that clear to me; it seems to only run when a subject has entered, but if you had two subjects and removed one this would it not also stop, despite there being another subject stil present? -->

:::workflow
![Aeon.Foraging.PelletMonitorWorkflow](../../workflows/pelletMonitorWorkflow.bonsai)
:::

#### Inputs
None

#### Outputs
Sequence of dynamic class events triggered by deliver pellet commands and beam break events, consisting of a "Timestamp" (`double`) and a "Value" (`boolean`) that reports the current state. 
This "Value" is `True` if when a delivery command has been received, and `False` when a successful beam break is detected. 

#### Properties
##### Subjects
Commands (inputs) to the `PelletMonitor` node are published to shared `Subject`s, the names of which are configured in the properties of the node. 

###### Device command subjects
| Subject name      | Type        | Description                   |
|-------------------|-------------|-------------------------------|
| **PelletCommand** | `Harp.HarpMessage`  | The name of the shared `Subject` carrying all events published by the [output expander](https://github.com/harp-tech/device.outputexpander) connected to an [`UndergroundFeeder`](#undergroundfeeder), e.g. "Patch1Events" |
| **PelletDelivered**| `Harp.Timestamped<bool>` | The name of the shared `Subject` carrying beam break events indicating successful pellet deliveries, e.g. "Patch1PelletDelivered". Also published by [`UndergroundFeeder`](#undergroundfeeder) |

#### Usage
To use a `PelletMonitor (Aeon.Foraging)` node, simply place one and configure its properties. 

:::workflow
![Aeon.Foraging.PelletMonitor](../../workflows/pelletMonitor.bonsai)
:::

### TimeSpentOnWheel 
The `TimeSpentOnWheel (Aeon.Foraging)` node monitors the motion of a given foraging wheel and accumulates the total time the animal is actively turning the wheel.
<!-- TODO: Fix link to wheelmoving.md -->
Within this node, the [`WheelMoving (Aeon.Acquisition)`](../../wheelMoving.md) node reports whether the wheel is in motion or not, and accumulates the differences between timestamps emitted by the feeder while the wheel is in motion.

:::workflow
![timeSpentOnWheelWorkflow](../../workflows/timeSpentOnWheelWorkflow.bonsai)
:::

#### Inputs
None

#### Outputs
Sequence of `double` values carrying the number of seconds the wheel has been in motion, accumulated from the data timestamps.

#### Properties
##### General
| Property name | Description                                               |
|---------------|-----------------------------------------------------------|
| **Name**      | Set the name to identify this specific dispenser module, e.g. "Patch1" |

##### Subjects
Commands (inputs) to the `TimeSpentOnWheel ` node are published to shared `Subject`s, the names of which are configured in the properties of the node. 
<!-- To be completed 
###### Device event subjects 
`HarpMessage` events emitted to a `Subject`

| Subject name      | Type        | Description                   |
|-------------------|-------------|-------------------------------|
| **Event1**        | `Type`      | Description of Event1         |
| **Event2**        | `Type`      | Description of Event2         |

###### Other output subjects
Other subjects published or updated by the node, usually ater some processing

| Subject name      | Type          | Description                                                                                     |
|-------------------|---------------|-------------------------------------------------------------------------------------------------|
| **Output1**       | `Type`        | Description of Output1                                                                          |
| **Output2**       | `Type`        | Description of Output2                                                                          |

###### Device command subjects 
Existing subjects published outside of the node, but used for input / trigger

| Subject name      | Type          | Description                                                                                     |
|-------------------|---------------|-------------------------------------------------------------------------------------------------|
| **Command1**      | `Type`        | Description of Command1                                                                         |
| **Command2**      | `Type`        | Description of Command2                                                                         |
-->
#### Usage 
<!-- TODO: Fix link to RepeatEveryBlock -->
To reset a `TimeSpentOnWheel (Aeon.Foraging)` monitor after a block transition, use a [`RepeatEveryBlock (Aeon.Acquisition)`](./RepeatEveryBlock.md) node and pass the result to an appropriately named `BehaviorSubject`, e.g. "Patch1TimeSpent".

:::workflow
![timeSpentOnWheel](../../workflows/timeSpentOnWheel.bonsai)
:::

### TimeSinceLastEvent 
The `TimeSinceLastEvent (Aeon.Foraging)` node monitors the current state of pellet delivery commands and the beam break.
<!-- Is this the correct workflow? -->
:::workflow
![Aeon.Foraging.PelletMonitorWorkflow](../../workflows/pelletMonitorWorkflow.bonsai)
:::

#### Inputs
None

#### Outputs
Sequence of `double` values carrying the number of seconds since the wheel was last turned, accumulated from the data timestamps

#### Properties
This node does not have any properties. 
However, it assumes that a "VideoEvents" `Subject` from a [`CameraController`](target-node-cameracontroller) node exists to monitor timestamps.

#### Usage
<!-- To be completed -->

### Additional nodes to be added
- [ ] `RepeatEveryBlock`
- [ ] `TimeSinceLastEvent`
- [ ] `PatchDistanceState`
- [ ] `PatchState`
- [ ] `PathDeliveryCount`
- [ ] `PatchTimeSpent`
- [ ] `PatchTimeSinceLastVisit`
- [ ] `PatchWheelDisplacement`

## GUI
<!-- To be completed -->

## Logging
Outputs from auxiliary nodes are first formatted using the `Format` node, within which the register addresses are configured for software generated data logs.
Utilising available registers of the output expander, the formatted outputs are then combined to form a "Patch" assembly, before being passed to the[`LogHarpState (Aeon.Acquisition)`](target-node-logharpstate) node to be written to a log file.

:::workflow
![logPatchEvents](../../workflows/logPatchEvents.bonsai)
:::

:::{note}
Register address 203 is not shown in this workflow, but is generated as events marked as a retry following an unsuccessful delivery attempt. 
This is passed to the "PatchEvents" `Subject` within the [`UndergroundFeeder (Aeon.Foraging)`](#undergroundfeeder) node.
:::

**Data schema**

| Register name         | Access | Address | Type    | Mask type          | Description                                   |
|-----------------------|--------|---------|---------|--------------------|-----------------------------------------------|
| **TimestampSeconds**          | Event  | 8       | U32    | -                             | Heartbeat                                       |
| **AuxInState**                | Event  | 32      | U8     | AuxiliaryInputs               | State of beam break                             |
| **OutputSet**                 | Write  | 35      | U8     | DigitalOutputs                | Deliver pellet command                          |
| **OutputClear**               | Write  | 36      | U8     | DigitalOutputs                | Deliver pellet command has been cleared         |
| **ExpansionBoard**            | Event  | 87      | U8     | ExpansionBoardType            | Should always be 1 (MagneticEncoder)            |
| **MagneticEncoder**           | Event  | 90      | U16    | [Angle, Magnitude]            | Reported angle and magnitude of magnetic encoder|
| **MagneticEncoderSampleRate** | Event  | 91      | U8     | MagneticEncoderSampleRateMode | Should always be 4 (500Hz)                      |
| **(dispenser_state)**        | -      | 200     | F32    | -                             | The current state of the pellet dispenser       | TODO
| **(delivery_manual)**         | -      | 201     | U8     | -                             | Manual pellet delivery events log               |
| **(missed_pellet)**           | -      | 202     | U8     | -                             | Missed pellet events log                        |
| **(delivery_retry)**          | -      | 203     | U8     | -                             | Missed pellet events log                        |

## State persistence
To ensure robustness and enable recovery from system crashes or other errors in long-term experiments, the state of the experiment can be stored in a `StateRecoverySubject` that persists over multiple executions of the same workflow.

Two of these subjects are initially declared per patch, at the highest level of the workflow. 
For instance, `Patch1State` stores the state of the patch itself, including the current wheel displacement and the foraging threshold of the associated dispenser module, `Patch1Dispenser`.

The state of a patch includes: 
- The distance the wheel has been turned, 
- the current threshold set for pellet delivery, 
- the total number of pellets delivered, and 
- the number of pellets still present in the feeder.

## Alerts
<!-- To be completed -->