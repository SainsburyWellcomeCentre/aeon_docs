(target-node-timespentonwheel)=
# TimeSpentOnWheel 
The `TimeSpentOnWheel (Aeon.Foraging)` node monitors the motion of a given foraging wheel and accumulates the total time the animal is actively turning the wheel.
<!-- TODO: Add link to wheelmoving.md when available -->
Within this node, the `WheelMoving (Aeon.Acquisition)` node reports whether the wheel is in motion or not, and accumulates the differences between timestamps emitted by the foraging patch while the wheel is in motion.

:::workflow
![timeSpentOnWheelWorkflow](../../../../workflows/timeSpentOnWheelWorkflow.bonsai)
:::

## Inputs
None

## Outputs
Sequence of `double` values carrying the number of seconds the wheel has been in motion, accumulated from the data timestamps.

## Properties
### General
| Property name | Description                                               |
|---------------|-----------------------------------------------------------|
| **Name**      | Set the name to identify this specific dispenser module, e.g. "Patch1" |

### Subjects
Commands (inputs) to the `TimeSpentOnWheel` node are published to shared `Subject`s, the names of which are configured in the properties of the node. 
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
## Usage 
<!-- TODO: Add link to RepeatEveryBlock.md when available -->
To reset a `TimeSpentOnWheel (Aeon.Foraging)` monitor after a block transition, use a `RepeatEveryBlock (Aeon.Acquisition)` node and pass the result to an appropriately named `BehaviorSubject`, e.g. "Patch1TimeSpent".

:::workflow
![timeSpentOnWheel](../../../../workflows/timeSpentOnWheel.bonsai)
:::