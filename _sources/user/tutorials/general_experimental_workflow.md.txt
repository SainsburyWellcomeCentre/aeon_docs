# General Experimental Workflow Infrastructure
The Harp hardware eco-system underpins the Aeon system. 
A full setup consists of multiple [Harp](https://www.cf-hw.org/harp) devices (e.g. [CameraController](https://github.com/harp-tech/device.cameracontrollergen2), [ClockSynchronizer](https://github.com/harp-tech/device.clocksynchronizer), etc.) and cameras that need to be monitored, controlled, and logged in synchrony. 
This tutorial provides an overview of the experimental workflow infrastructure and the general strategy for designing workflows using [`Aeon.Acquisition`](target-acquisition-modules) nodes in [Bonsai](https://bonsai-rx.org/).

## Harp device configuration
Each physical Harp device used in Aeon has a dedicated [`IncludeWorkflow`](https://bonsai-rx.org/docs/api/Bonsai.Expressions.IncludeWorkflowBuilder.html) in the [`Aeon.Acquisition`](target-acquisition-modules) package. 
For example, a Harp [CameraController (Gen2)](https://github.com/harp-tech/device.cameracontrollergen2) device is controlled by a [`CameraController (Aeon.Video)`](target-node-cameracontroller) node.
In the main experimental workflow, nodes are each placed in `Metadata` > `Devices` of the [`GroupWorkflow`](https://bonsai-rx.org/docs/api/Bonsai.Expressions.GroupWorkflowBuilder.html). 
Upon execution, these nodes connect to the corresponding physical devices and configure their operation settings according to the specified properties of the node.
Additionally, the triggers and functions of any triggered actions on the device (e.g. delivering a food pellet) as well as any [`Subject`](https://bonsai-rx.org/docs/articles/subjects.html) names used as inputs and outputs to the device are defined here.

Events emitted by Harp devices are in the form of `Harp.HarpMessages`. 
The full event stream, along with other useful outputs are published to `Subjects` or `BehaviorSubjects`, making them accessible in the Bonsai editor's toolbox anywhere in the workflow using their names.

## Soft devices
- tracking
- synch monitor
- pose tracking
- active regions
- light intensity
- light server

## GUI
Many of the outputs from these devices, for example, a camera, are useful to observe live from a control panel. 
This is achieved through the visualiser functionality of Bonsai.

## Challenges in long-term multidimensional data acquisition
Acquiring data over extended periods necessitates robust strategies to handle rare system failures, ensuring minimal loss of time and data. 
Effective logging and data management is crucial for addressing potential bottlenecks and storage limitations, as well as to enable efficient data transfer to long-term storage solutions. 
Additionally, semi-automated monitoring systems are essential for overseeing the health and status of animal subjects and the experiment, as continuous 24-hour human surveillance is impractical.

## State persistence
One challenge of long-term experiments is the potential for rare events of system instability, such as a power cut, interrupting acquisition. 
To ensure the workflow is robust against these events, the `StateRecoverySubject` is a special type of `Subject` that persists across multiple executions of the same workflow. 
This feature can be used to automatically restore the state of the system following a crash, allowing acquisition and control to resume seamlessly.

## Alerts
In long-term experiments, it is crucial to maintain stable and consistent hardware and data acquisition. 
When animal subjects are involved, continuous monitoring of their health and status becomes necessary to ensure compliance with legal and ethical standards.
However, continuous human monitoring is impractical. 
To address this, the Aeon system is equipped with an automated [alert](target-module-alerts) feature that notifies select groups of people through an incoming webhook service. 
For instance, if a camera stream is lost or if an animal is no longer detected, the system can alert team members via a Microsoft Teams channel or other webhook services. 
This ensures that critical hardware failures and warnings are promptly addressed.

## Logging
### Experimental configuration 
<!-- need more details on the metadata file content -->
Each experimental workflow is configured via a `metadata.yml` file, saved alongside the data in a timestamped data folder.

### Data chunking
To manage a continuous stream of data of undetermined length, the workflow is configured to save data locally. 
All logs and data are grouped and saved in 1-hour long {term}`chunks <acquisition chunk>`. 
Each chunk is defined by the Harp system time, i.e. the [ClockSynchronizer](https://github.com/harp-tech/device.clocksynchronizer) device, and is created every hour, on the hour, in real time.

### Robocopy
An automated file transfer service, [Robocopy](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy), is used to periodically transfer locally saved data to a dedicated storage server on the Sainsbury Wellcome Centre (SWC) network. 
This ensures data files are kept at a manageable size and enables continuous data acquisition without the concern of reaching local disk storage limits.

### Naming/format convention and analysis API compatibility
The Aeon data architecture is designed to be simple and standardised across Harp devices and data streams. 
To facilitate this, Aeon's [Python packages](target-repositories), `aeon_api` and `aeon_mecha` provide a comprehensive suite of tools for data ingestion, reading, and analysis. 
This ensures that data stored in the standardised format can be efficiently accessed and processed, supporting seamless integration and analysis across different components of the Aeon system.

### Data streams
- **Harp devices**: Logs for each individual Harp device are stored in `.bin` files
- **Camera video streams**: Video frames are triggered in synchrony by a Harp `CameraController` and are logged as `.avi` files, along with `.csv` files containing the "FrameID" and Harp "Timestamp" for each frame
- **Data streams**: Any `Harp.Timestamped` stream of data whose members can be stored in `.csv` format.