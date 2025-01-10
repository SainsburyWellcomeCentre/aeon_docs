(target-module-foraging-patch)=
# Foraging Patch

The foraging patch module is core to foraging and long-term 24/7 experiments. 
It is utilised with a [feeder](target-feeder) hardware module assembly and a [Harp output expander](https://github.com/harp-tech/device.outputexpander) to provide a means for the animals in the arena to obtain food with a configurable wheel the animal can turn, simulating a naturalistic digging action. 

## Nodes
### UndergroundFeeder
The `UndergroundFeeder (Aeon.Foraging)` node establishes a connection to the [feeder](target-feeder) hardware module assembly through a Harp output expander. 
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
| **PortName**  | The COM port the output expander attached to your feeder is connected to.                                                     |
| **Radius**    | The radius of the foraging wheel in centimeters. This is used to compute the distance the wheel has been turned. Our foraging patch wheel has a radius of 4cm |
| **SampleRate**| The sampling rate of the magnetic encoder monitoring the wheel, selected from options available. For aeon experiments, this is set to 500Hz. |

##### Retry function
If a pellet is due to be delivered, an IR beam break module in the feeder detects whether the pellet delivery is successful. 
In the event that a pellet is not delivered (no beam break detected), then the feeder can be configured to try again. 
These properties configure the options around this functionality.

| Property name | Description                                   |
|---------------|-----------------------------------------------|
| **DueTime**   | The time following a pellet delivery command that the device will wait for a successful beam break signal before assuming the pellet delivery has failed. |
| **Count**     | The number of retry attempts the feeder will perform. |

##### Subjects
Events and commands from the feeder are collected from, and published to shared `Subjects`, in some cases after some processing. 
Here you set the names used for these `Subjects` to identify events, commands or datastreams for this specific feeder. 
Each of these subjects becomes accessible in the bonsai editor's toolbox anywhere in the workflow using the name set here.

###### Device events subjects
| Subject name      | Type        | Description                   |
|-------------------|-------------|-------------------------------|
| **PatchEvents**      | `Harp.HarpMessage`       | Contains all events, consisting of timestamped Harp messages reporting the state of each register of the output expander. Also output directly by the `UndergroundFeeder` node.|
| **WheelDisplacement**| `Harp.Timestamped<double>`| The sample-to-sample displacement of the foraging wheel in mm.           |
| **PelletDelivered**  | `Harp.Timestamped<bool>`  | Reports `True` when a pellet is detected by the IR beam break register. |

###### Device command subjects
| Subject name      | Type          | Description                                                                                     |
|-------------------|---------------|-------------------------------------------------------------------------------------------------|
| **DeliverPellet**    | `object`   | Trigger pellet delivery. Any event passed to this `Subject` will trigger a pellet delivery      |
| **ResetFeeder**      | `object`   | Trigger feeder reset. Any event passed to this `Subject` will trigger a feeder reset |

#### Usage
Create a `GroupWorkflow` and give it an appropriate name e.g. `"Patch1"`. 
Inside, place an `UndergroundFeeder (Aeon.Foraging)` node, externalise all properties, and connect it to the `WorkflowOutput`:

![Aeon.Foraging.UndergroundFeeder](./Workflows/base-feeder.svg)

### PatchDispenser 
The `PatchDispenser` node keeps track of the number of pellets available to the feeder. 
It accepts pellet discount notifications triggered by the IR beam break following successful pellet delivery, and discounts these from the total number of pellets, which is itself set manually when loading the feeder hopper.

#### Inputs
`Harp.Timestamped<bool>` events emitted by the `UndergroundFeederModule` indicating pellet delivery. 

#### Outputs
Stream of custom class `Aeon.Foraging.DispenserEventArgs`. 
<!-- TODO: Fix link to controlpanel -->
Each item emitted consists of a "Value" (`int`) corresponding to the pellet count following an event, and an "EventType" (`Aeon.Foraging.DispenserEventType`) describing the reason for the new pellet count, i.e. due to a triggered "Discount", or "Reset" or "Refill" command from the [control panel](../../GUI/controlPanel.md).

#### Properties
##### General
| Property name | Description                                               |
|---------------|-----------------------------------------------------------|
| **Name**      | Set the name to identify this specific dispenser module. e.g. "Patch1" |

##### Subjects <!-- Description copied from previous section -->
Events and commands from the feeder are collected from, and published to shared `Subjects`, in some cases after some processing. 
Here you set the names used for these `Subjects` to identify events and commands for this node for a specific feeder. 
Each of these subjects becomes accessible in the bonsai editor's toolbox anywhere in the workflow using the name set here.

###### Device events subjects <!-- Missing category header, check if this is the correct category -->
| Subject name      | Type        | Description                   |
|-------------------|-------------|-------------------------------|
| **ControllerEvents** | `Aeon.Foraging.DispenserEventArgs` | Controller events shared `Subject`, carrying the number of pellets remaining (`int`) and the `EventType`. Also output directly by the node. |
| **DispenserState** |   | Declared `StateRecoverySubject` to store the current number of pellets. |

#### Usage
Place a `SubscribeSubject` and point it to the "PelletDelivered" `Subject` for a patch (e.g. "Patch1PelletDelivered"). 
Connect this to a `Condition` node that checks the `Value` of the incoming `Subject`. 
This is a `Boolean` that reports `True` on pellet delivery, and ensures only the rising edge of this signal is counted as a delivery. 
Finally, connect this to a `PatchDispenser (Aeon.Foraging)` node.

![Aeon.Foraging.PatchDispenser](./Workflows/patchDispenser.svg)

### PelletMonitor 
The `PelletMonitor` node monitors the current state of pellet delivery commands and the beam break. 
<!-- Moved this out from Usage, as it seems to be explaining what's going on under the hood. 
Why do we "expand" and show the workflow here and not for others? 
Are users expected to copy and paste this? -->
Inside this node, pellet delivery commands received by the Harp output expander are filtered from the "PatchEvents" `Subject` and successful deliveries monitored through the "PelletDelivered" `Subject` (e.g. "Patch1PelletDelivered"). 
The `RepeatEverySubject` node ensures this node is only running while an animal is present in the arena. <!-- This is not that clear to me; it seems to only run when a subject has entered, but if you had two subjects and removed one this would it not also stop, despite there being another subject stil present? -->

![Aeon.Foraging.PelletMonitorWorkflow](./Workflows/pelletMonitorWorkflow.svg)

#### Inputs
None

#### Outputs
Sequence of dynamic class events triggered by deliver pellet commands and beam break events, consisting of a "Timestamp" (`double`) and a "Value" (`boolean`) that reports the current state. 
This "Value" is `True` if when a delivery command has been received, and `False` when a successful beam break is detected. 

#### Properties
##### Subjects <!-- Description copied from previous section -->
Events and commands from the feeder are collected from, and published to shared `Subjects`, in some cases after some processing. 
Here you set the names used for these `Subjects` to identify events for this node for a specific feeder. 
Each of these subjects becomes accessible in the bonsai editor's toolbox anywhere in the workflow using the name set here.

###### Device events subjects <!-- Missing category header, check if this is the correct category -->
| Subject name      | Type        | Description                   |
|-------------------|-------------|-------------------------------|
| **PelletCommand** | The name of the shared `Subject` carrying all events published by the [output expander](https://github.com/harp-tech/device.outputexpander) connected to an [`UndergroundFeeder`](#undergroundfeeder-node). e.g. 'Patch1Events'  |
| **PelletDelivered**   | The name of the shared `Subject` carrying beam break events indicating successful pellet deliveries, e.g. 'Patch1PelletDelivered'. Also published in [`UndergroundFeeder`](#undergroundfeeder-node) |

#### Usage
To use a `PelletMonitor (Aeon.Foraging)` node, simply place one and configure its properties. 

![Aeon.Foraging.PelletMonitor](./Workflows/pelletMonitor.svg)

### TimeSpentOnWheel 
A brief description of what the node does.

#### Inputs
#### Outputs
A sequence of `<type>` with the following attributes. 
| Attribute name     | Type                           | Description                      |
|--------------------|--------------------------------|----------------------------------|
| **Attr1**          | `Type`                         | Description of Attr1             |
| **Attr2**          | `Type`                         | Description of Attr2             |

#### Properties
##### General
| Property name | Description                                               |
|---------------|-----------------------------------------------------------|
| **Property1** | Description of Property1                                  |
| **Property2** | Description of Property2                                  |

##### Other option category or function
| Property name | Description                                   |
|---------------|-----------------------------------------------|
| **Option1**   | Description of Option1                        |
| **Option2**   | Description of Option2                        |

##### Subjects
An overview of the events and commands available or published to `Subject`s

###### Device events subjects
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

#### Usage
Instructions for creating and configuring the main device node. Add necessary sub-components and configurations.

![InsertWorkflow](path/to/workflow.svg)

### TimeSinceLastEvent 
A brief description of what the node does.

#### Inputs
#### Outputs
A sequence of `<type>` with the following attributes. 
| Attribute name     | Type                           | Description                      |
|--------------------|--------------------------------|----------------------------------|
| **Attr1**          | `Type`                         | Description of Attr1             |
| **Attr2**          | `Type`                         | Description of Attr2             |

#### Properties
##### General
| Property name | Description                                               |
|---------------|-----------------------------------------------------------|
| **Property1** | Description of Property1                                  |
| **Property2** | Description of Property2                                  |

##### Other option category or function
| Property name | Description                                   |
|---------------|-----------------------------------------------|
| **Option1**   | Description of Option1                        |
| **Option2**   | Description of Option2                        |

##### Subjects
An overview of the events and commands available or published to `Subject`s

###### Device events subjects
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

#### Usage
Instructions for creating and configuring the main device node. Add necessary sub-components and configurations.

![InsertWorkflow](path/to/workflow.svg)

## GUI
Description of any user interface components and visualisers.

## Logging
Information on logging functionalities, nodes involved, and schemas for recorded data.

**Data schema**

| Register name         | Access | Address | Type    | Mask type          | Description                                   |
|-----------------------|--------|---------|---------|--------------------|-----------------------------------------------|
| **Register1**         | Access | Address | `Type`  | Mask               | Description of Register1                      |
| **Register2**         | Access | Address | `Type`  | Mask               | Description of Register2                      |

(For not virtual harp devices) a full list of the available registers for the `device name` see the corresponding [device.yml](link-to-harprepo-device.yml)

## State persistence
Information on state recovery or persistence requirements, if applicable.

## Alerts
Explanation of any alert configurations and links to guides or further configuration steps.