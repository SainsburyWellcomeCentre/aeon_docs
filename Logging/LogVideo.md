# **LogVideo**

The `LogVideo` node saves harp timestamped video frames in `.avi` format, with the correspoonding unique index ID and timestamp for each frame stored in corresponding `.csv` files. Both follow the file naming convention of Project AEON. 
```
"<CameraStreamName>_<chunkTimestamp>.<ext>"`
```
For example: 
```
"CameraTop_2024-06-27T10-00-00.avi"
"CameraTop_2024-06-27T10-00-00.csv"
```

It is generally the terminal node of a Bonsai workflow branch, with the typical pattern to subscribe to a specific frame events subject, and pass directly to this node: 

![workflowImage](./Workflows/logVideo.svg)

Data is grouped into 1 hour long chunks for continuous logging. This function is dependent on signals from the `ClockSynchronizer`. See the [guide](../HardwareDevices/ClockSynchronizer/clocksynchronizer.md) for more information to set this device up in your workflow.

### Inputs and Outputs:

- **Inputs**:
Stream of `Harp.Timestamped<Aeon.Acquisition.VideoDataFrame>`, originating from a `SpinnakerVideoSource (Aeon.Acquisition)` node, described in the [camera guide](../HardwareDevices/Camera/camera.md).

- **Outputs**:
Stream of raw video images of type `OpenCV.Net.IPlImage`. 
## **Properties of the node:**
### ***GroupClosing:***

| **Property Name**   | **Description**                                                                              |
|---------------------|----------------------------------------------------------------------------------------------------|
| **ClosingDuration** | *Description missing*                                                                              |
| **Heartbeats**      | The name of the subject carrying the `TimestampSeconds` events from the `ClockSynchronizer` that the system is synchronized with. |

### ***Misc:***

| **Property Name**   | **Description**                                                                                    |
|---------------------|----------------------------------------------------------------------------------------------------|
|**LogName**          | The name of this log. This will determine the naming of a dedicated folder and data files.         | 