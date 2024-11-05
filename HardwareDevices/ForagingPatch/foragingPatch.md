# **Foraging Patch Module**

The foraging patch module provides a means for the subjects in the arena to obtain food with a configurable wheel the subject can turn, simulating a naturalistic digging motion. The device design, schematic and assembly instructions can be found here [link]()

This guide will walk through how a feeder device and associated modules are added and configured; the outputs, control and logging workflows, as well as modules that are important to make long-term 24/7 experiments possible with limited human intervention. 

## <u>UndergroundFeeder node:</u>
### **Device configuration**

Create a `GroupWorkflow` and give it an appropriate name e.g. `"Patch1"`. 
Inside, place an `Aeon.Foraging.UndergroundFeeder` node in your workflow, externalise all properties, and connect it to the `WorkflowOutput`:

![Aeon.Foraging.UndergroundFeeder](./Workflows/base-feeder.svg)

This node establishes a connection to the feeder hardware module assembly through a [Harp output expander](https://github.com/harp-tech/device.outputexpander). It also defines the basic functions of the feeder and a workflow to configure the relevant device operation properties. The device uses the standardised harp communication protocol, producing timestamped harp messages when device events occur.

### Inputs and Outputs:

**Inputs** - None

**Outputs** - Stream of all `Harp.HarpMessages` emitted by this harp device.

--------
### **Properties of the Node:**

#### ***General:***
These properties are critical parameters for the operation of the device.

| Property Name | Description                                                                                                                   |
|---------------|-------------------------------------------------------------------------------------------------------------------------------|
| **PortName**  | The COM port the output expander attached to your feeder is connected to.                                                     |
| **Radius**    | The radius of the foraging wheel in centimeters. This is used to compute the distance the wheel has been turned. Our foraging patch wheel has a radius of 4cm |
| **SampleRate**| The sampling rate of the magnetic encoder monitoring the wheel, selected from options available. For aeon experiments, this is set to 500Hz. |

#### ***Retry Function:***
If a pellet is due to be delivered, an IR beam break module in the feeder detects whether pellet delivery is successful. In the event that a pellet is not delivered (no beam break detected), then the feeder can be configured to try again. These properties configure the options around this functionality.

| Property Name | Description                                                                                                                   |
|---------------|-------------------------------------------------------------------------------------------------------------------------------|
| **DueTime**   | The time following a pellet delivery command that the device will wait for a successful beam break signal before assuming the pellet delivery has failed. |
| **Count**     | The number of retry attempts the feeder will perform.                                                                         |


### ***Subject names:***
Events and commands from the feeder are collected, in some cases processed, and published to `Subjects`. Here you set the names used for these `Subjects` to identify events, commands or datastreams for this specific feeder. Each of these subjects become accessible in the bonsai editor's toolbox anywhere in the workflow using the name set here.

## <u>Subjects</u>
### **Device Event Subjects**:
| Subject Name          | Type                    | Description                                                                                                  |
|----------------------|--------------------------|--------------------------------------------------------------------------------------------------------------|
| **PatchEvents**      | `Harp.HarpMessage`       | Contains all events, consisting of timestamped Harp messages reporting the state of each register of the output expander. Also output directly by the `UndergroundFeeder` node.|
| **WheelDisplacement**| `Harp.Timestamped<double>`| The sample to sample displacement of the foraging wheel.                                                    |
| **PelletDelivered**  | `Harp.Timestamped<bool>`  | Reports `True` when a pellet is detected by the IR beam break register.                                     |


### **Device Command Subjects**:
| Subject Name          | Type                     | Description                                                                                                 |
|----------------------|--------------------------|--------------------------------------------------------------------------------------------------------------|
| **DeliverPellet**    | `object`                  | Trigger pellet delivery. Any event passed to this `Subject` will trigger a pellet delivery                  |
| **ResetFeeder**      | `object`                  | Trigger feeder reset. Any event passed to this `Subject` will trigger a feeder reset                        |

# <u>Auxiliary Modules</u>

Many measures are crucial to keep track of, both to display in visualisers as the experiment progresses and for logging events, experimental parameters and behavioral quantifications of interest. So far, the hardware is configured, but some processing of the sensor data and events from the device is required to extract useful measures in real time. Auxiliary modules are used in Bonsai to extend the functionality of this device and create a full foraging assembly, which we call a "Patch". For each patch, we track:

- PelletCount
- TimeSpentOnPatches
- TimeSinceLastVisit
- TotalDistanceTravelled
- MissedPellets
- ManualPellets
- TotalPelletsDelivered

## <u>**Patch Dispenser:**</u>
![Aeon.Foraging.PatchDispenser](./Workflows/patchDispenser.svg)

This module keeps track of the number of pellets available to the feeder. It accepts pellet discount notifications triggered by the IR beam break following successful pellet delivery, and discounts these from the total number of pellets, which is itself set manually when loading the feeder hopper.

## Inputs and Outputs:

**Inputs** - `Harp.Timestamped<bool>`. Events emitted by the `UndergroundFeederModule` indicating pellet delivery. 

**Outputs** - Stream of custom class `Aeon.Foraging.DispenserEventArgs`. Each item emitted consists of a Value (`int`) corresponding to the pellet count following an event, and an Event type (`Aeon.Foraging.DispenserEventType`). 

## **Properties of the node:**

### ***General:***

| Property Name | Description                                           |
|---------------|-------------------------------------------------------|
| **Name**      | Set the name of this dispenser module.                |

### ***Subject names:***
Set the names used for these subjects to identify these events, commands or datastreams for this specific feeder. Each of these subjects is published and become accessible in the bonsai editor's toolbox anywhere in the workflow using this name.

## <u>Subjects</u>:

| Property Name         | Description                                              |
|----------------------|-----------------------------------------------------------|
| **ControllerEvents** | Controller events shared `Subject`.   |
| **DispenserState**   | Declared `StateRecoverySubject` to store the dispenser state. |

### <u>**Workflows**</u>
- [ ] **PelletMonitor**

![Aeon.Foraging.PelletMonitor](./Workflows/pelletMonitor.svg)
- [ ] **TimeSpentOnWHeel**
- [ ] **RepeatEveryBlock**
- [ ] **TimeSinceLastEvent**


### <u>**Subjects**</u>
- [ ] `PatchDistanceState`
- [ ] `PatchState`
- [ ] `PathDeliveryCount`
- [ ] `PatchTimeSpent`
- [ ] `PatchTimeSinceLastVisit`
- [ ] `PatchWheelDisplacement`


### <u>GUI</u>

### <u>Logging</u>

In the  case of a feeder, outputs from auxiliary modules are combined to form a "Patch" assembly, utilising available registers of the output expander. Note the use of the `Format` node to configure the register addresses for software generated data logs. Logging of this harp device is performed using the  [`LogHarpState (Aeon.Acquisition)`](../../Logging/LogHarpState.md) node.  

![logPatchEvents](./Workflows/logPatchEvents.svg")

Register address 203 is not shown in this workflow, but is generated as events marking a delivery command as a retry attempt, and passed to the `PathEvents` ` Subject` within the by the `UndergroundFeeder` node.

*Data Schema*:
| Register Name             | Access | Address | Type   | Mask Type / Attributes        | Description                                     |
|---------------------------|--------|---------|--------|-------------------------------|-------------------------------------------------|
| TimestampSeconds          | Event  | 8       | U32    | -                             | Heartbeat                                       |
| AuxInState                | Event  | 32      | U8     | AuxiliaryInputs               | State of beam break                             |
| OutputSet                 | Write  | 35      | U8     | DigitalOutputs                | Deliver pellet command                          |
| OutputClear               | Write  | 36      | U8     | DigitalOutputs                | Deliver pellet command has been cleared         |
| ExpansionBoard            | Event  | 87      | U8     | ExpansionBoardType            | Should always be 1 (MagneticEncoder)            |
| MagneticEncoder           | Event  | 90      | U16    | [Angle, Magnitude]            | Reported angle and magnitude of magnetic encoder|
| MagneticEncoderSampleRate | Event  | 91      | U8     | MagneticEncoderSampleRateMode | Should always be 4 (500Hz)                      |
| (dispenser_state)         | -      | 200     | F32    | -                             | The current state of the pellet dispenser       | TODO
| (delivery_manual)         | -      | 201     | U8     | -                             | Manual pellet delivery events log               |
| (missed_pellet)           | -      | 202     | U8     | -                             | Missed pellet events log                        |
| (delivery_retry)          | -      | 203     | U8     | -                             | Missed pellet events log                        |

### <u>State persistence</u>

In order to be robust and enable recovery from system crashes or other errors in long term experiments, the state of the experiment can be stored in a `StateRecoverySubject` that persists over multiple executions of the same workflow.

Two of these subjects are initially declared per patch, at the highest level of the workflow. These store the state of the patch itself `Patch1State`, for instance, which carries the current wheel displacement, threshold and and of the associated dispenser module `Patch1Dispenser`

The state of the Patch module includes the distance the wheel has been turned, the current threshold set for pellet delivery, the total number of pellets delivered and still present in the feeder.

### <u>Alerts</u>