# Video Controller for multiple camera system

A harp [CameraController (Gen2)](https://github.com/harp-tech/device.cameracontrollergen2) device is utilised to configure and synchronously trigger two sets of cameras which can operate at different framerates. [Camera.md](../Camera/camera.md) details how to add a camera controlled by this VideoController.

This guide documents how the camera controller device is added and configured; the outputs, control and logging and alert workflows.

## <u>Device configuration</u>

### CameraController node:

Create a `GroupWorkflow` with an appropriate name e.g. `"VideoController"`. 
Inside, place a `CameraController (Aeon.Acquisition)` node, externalise all properties, and connect it to the `WorkflowOutput`:

![Aeon.Acquisition.CameraController](./Workflows/videoController.svg)

This node establishes a connection to the Camera Controller, allowing direct control to start and stop connected cameras, and configuration of the frequency of the camera triggers. The controller hardware will generate two timestamped camera trigger event streams to synchronously trigger two sets of one or many cameras. 

## **Properties of the node:**
### **General**

| **Property** | **Description**                                               |
|--------------|---------------------------------------------------------------|
| **PortName** | The COM port the physical CameraController is connected to.    |

### **Camera trigger configuration**

| **Property**              | **Description**                                                |
|---------------------------|----------------------------------------------------------------|
| **GlobalTriggerFrequency** | Set the frequency of the first (global) set of camera frame triggers. |
| **LocalTriggerFrequency**  | Set the frequency of the second (local) set of camera frame triggers. |

## **Subjects:**
Events and commands from the feeder are collected, in some cases processed, and passed to published subjects. Here you set the names used for these subjects to identify these events, commands or datastreams for this specific feeder. Each of these subjects is published and become accessible in the bonsai editor's toolbox anywhere in the workflow using this name.

### **Device Events Subject**

| **Subject**       | **Type**                           |**Description**                           |
|-------------------|------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| **VideoEvents**   | `Harp.HarpMessage`  | A stream of all events emitted by the Harp [CameraController (Gen2)](https://github.com/harp-tech/device.cameracontrollergen2). Also directly output by the node. |

### **Other Output Subjects**

| **Subject**             | **Type**                                     | **Description**                                                                                   |
|-------------------------|----------------------------------------------|---------------------------------------------------------------------------------------------------|
| **GlobalTrigger**       | `Harp.CameraControllerGen2.CameraEvent`      | A stream of timestamped camera trigger events generated at the `GlobalTriggerFrequency`.          |
| **LocalTrigger**        | `Harp.CameraControllerGen2.CameraEvent`      | A stream of timestamped camera trigger events generated at the `LocalTriggerFrequency`.           |
| **GlobalTriggerFrequency** | `double`                                 | `BehaviorSubject` to store the value of `GlobalTriggerFrequency`.                                 |
| **LocalTriggerFrequency**  | `double`                                 | `BehaviorSubject` to store the value of `LocalTriggerFrequency`.                                  |

### **Device Command Subjects**

| **Subject**       | **Type**    |**Description**                                                                     |
|-------------------|-------------|------------------------------------------------------------------------------------|
| **StartCameras**  | `object`    | Any item sent to this `BehaviorSubject` immediately begins camera  acquisition.    |
| **StopCameras**   | `object`    | Any item sent to this `BehaviorSubject` immediately stops camera acquisition.      |


## GUI
None
## Logging
All events are logged using a [`LogHarpState (Aeon.Acquisition)`](../../Logging/LogHarpState.md) node.

![Aeon.Acquisition.LogHarpState](./Workflows/logVideoEvents.svg)

This will log the state of all relevant harp registers in a dedicated folder. Logs can be identified by their register address, summarised here.

*Data Schema*:
| Register Name         | Access | Address | Type  | Mask Type          | Description                                   |
|-----------------------|--------|---------|-------|--------------------|-----------------------------------------------|
| TimestampSeconds      | Event  | 8       | U32   | -                  | Heartbeat                                     |
| Cam0Event             | Event  | 32      | U8    | CameraEvents       | Signals a frame was triggered on camera 0     |
| Cam1Event             | Event  | 33      | U8    | CameraEvents       | Signals a frame was triggered on camera 1     |
| ConfigureCam0Event    | Write  | 34      | U8    | EventConfiguration | Configures the event on camera 0              |
| ConfigureCam1Event    | Write  | 35      | U8    | EventConfiguration | Configures the event on camera 1              |
| StartAndStop          | Write  | 36      | U8    | CameraFlags        | Starts and stops the cameras immediately      |
| TriggerFrequencyCam0  | Write  | 45      | U16   | -                  | Specifies the trigger frequency for camera 0  |
| TriggerFrequencyCam1  | Write  | 52      | U16   | -                  | Specifies the trigger frequency for camera 1  |


For the full register and bitmask schema for the `CameraControllerGen2` see the corresponding [device.yml](https://github.com/harp-tech/device.cameracontrollergen2/blob/main/device.yml). 

## State persistence
Not required for state recovery
## Alerts
In Project AEON, The `VideoEvents` subject is useful for several environment monitoring workflows, such as regular logging of a summary of the current state of the experiment each hour. See the [alerts guide](../../Alerts/Alerts.md) to configure these alerts.

As with other harp devices in the system, this stream should be added to the `HeartbeatSources`, which are monitored to ensure continuous synchronization with all other synchronised devices on the system. See [synchronizer monitor guide](../../Alerts/) to configure these alerts.
