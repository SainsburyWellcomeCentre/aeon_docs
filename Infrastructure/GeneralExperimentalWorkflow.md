# Project Aeon General Experimental Workflow Infrastructure

A full experimental setup has several devices and cameras being monitored, controlled and logged in synchrony. Here is a general description of the strategy in designing workflows using Project Aeon nodes in Bonsai.

Individual articles on each specific device and how to integrate them into your workflow can also be found here.

## Device configuration

Each physical device, for example a [Clock Synchroniser](https://github.com/harp-tech/device.synchronizer) or [Camera Controller](https://github.com/harp-tech/device.cameracontrollergen2), has a dedicated `IncludeWorkflow` included in the `Aeon.Acquisition` package. From the main workflow, these are each placed inside the GroupWorkflows `Metadata`>`Devices`. When the workflow is executed, these nodes establish a connection with the physical device and configure its operation settings according to the specified properties of the node. Additionally, the triggers and function of any triggered actions on the device, delivering a food pellet for instance, as well as any subject names for inputs and outputs to the device are defined here.

Events emitted by the device are in the form of `Harp.HarpMessages`. The full event stream, along with other useful outputs are published to `Subjects` or `BehaviorSubjects` so are accessible from elsewhere in the workflow. 

## Soft devices
- tracking
- synch monitor
- pose tracking
- active regions
- light intensity
- light server

## GUI
Many of the outputs from these devices, for example a camera, are useful to observe live from a control panel. This is achieved through the visualiser functionality of Bonsai.

## Challenges in long-term multidimensional data acquisition.

Acquiring data over long time scales requires that specific considerations must be given to being robust to rare system failures, losing as little time and data as possible. In logging and data management, bottlenecks and blocks in storage space and data transfer to long term storage must be considered. It is also required to have semi-automated monitoring for the animal subjects and experiment status, where constant 24hr human surveillance is impractical.   

## State persistence
One challenge of long term experiments is the potential for rare events of system instability, like a power-cut, interupting acquisition. In order for the workflow to be robust to these events, the `StateRecoverySubject` is a special kind of `Subject` that persists across multiple executions of the same workflow. This feature can be used to automatically restore the state of the system following a system crash and continue acquisition and control seamlessly. 

## Alerts
Legally and ethically, recording animal subjects over timescales of weeks in an experimental arena requires that the health and status of the animals be under constant surveillance. In addition, constant human surveillance of these experiments to ensure the hardware and acquisition is stable and consistent is impractical. Instead, the AEON system is designed to send automated alerts to select groups of people through an incoming webhook service. In the event that, for example a camera stream is lost, or an animal can no longer be detected, this feature is used to alert team members through a Microsoft Teams channel, or other webhook service, to critical hardware failures and warnings. 

## Logging

### Experimental configuration:
The `'metadata.yml'` file saved with the data in a timestamped data folder carries the configuration of the experimental workflow.

### Data chunking
To manage a constant stream of data of undetermined lenght, the workflow saves data locally, with all logs and data grouped and saved in 'chunks' 1 hour long. Each chunk is defined by the harp system time, specifically by the `ClockSynchronizer` device and is created every hour, on the hour in real time.

### Robocopy
An automated file transfer service, 'Robocopy', is used to periodically transfer locally saved data to a dedicated storage server on the SWC network. This keeps data files a manageable size and enables continuous data acquisition without concern for reaching limits in local disk storage space.

### Naming / format convention and analysis API compatibility
The data architecture of Project AEON is designed to be simple and standardized across harp devices and data streams. The `aeon.mecha` and `aeon.analysis` repositories include a comprehensive API for ingestion, reading and analysis of data stored in this standardized format. 

### Logged data streams:
- **Harp devices**: The Harp hardware eco-system underpins the Aeon system, relying on harp devices for synchronisation and control across devices and cameras. Logs for each individual harp device are stored in `.bin` files
- **Camera video streams**: Video frames on a harp `CameraController` triggerare stored as `.avi` files, along with `.csv` files containing the frameID and harp timestamp for each frame.
- **Data streams**: Any `Harp.Timestamped` stream of data whose members can be stored in `.csv` format.
