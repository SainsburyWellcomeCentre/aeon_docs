(target-module-pose-estimation)=
# Pose Estimation
The pose estimation module utilises [SLEAP's](https://sleap.ai/) multi-animal tracking capabilities to simultaneously identify and track different animals within an arena. 
SLEAP is fully integrated with Bonsai through the [Bonsai.Sleap](https://bonsai-rx.org/sleap/index.html) package and enables real-time inference using a trained and exported model.

## Nodes
### PoseTracking
The `PoseTracking (Aeon.Vision.Sleap)` node loads a trained SLEAP model, and runs inference on frame events from a [camera](target-node-spinnakervideosource) device, returning timestamped data containing the position of each animal, their identity and confidence measures. 

<!-- To be completed
#### Inputs
#### Outputs
A sequence of `<type>` with the following attributes. 
| Attribute name     | Type                           | Description                      |
|--------------------|--------------------------------|----------------------------------|
| **Attr1**          | `Type`                         | Description of Attr1             |
| **Attr2**          | `Type`                         | Description of Attr2             |
-->
#### Properties
##### General
| Property name | Description                                               |
|---------------|-----------------------------------------------------------|
| **IdentityMinConfidence** |  Set the minimum confidence score applied to computation of an object (animal) instance's centroid |
| **FrameStep**           | Frame by frame inference and pose estimation is computationally expensive. It may be helpful to downsample the incoming stream to run inference in real time. Here you can set the number of frames to skip between incoming frames  |
| **IdentityMinConfidence** | Set the minimum confidence required to label an instance's identity |
| **ModelPath** | Set the partial path to the saved `frozen_graph.pb` |
| **PartMinConfidence** | Set the minimum confidence required to assign a label to an instance's keypoint |

##### Subjects
Both generated and input events of this node are collected and passed to published `Subjects`. 
Here you set the names used for these `Subjects` to identify events for this node.
Each of these `Subjects` becomes accessible in the Bonsai editor's toolbox anywhere in the workflow using the name set here.

###### Device event subjects
| Subject name      | Type        | Description                   |
|-------------------|-------------|-------------------------------|
| **TrackingEvents** | `Harp.Timestamped<Bonsai.Vision.ConnectedComponentCollection>` | The `Subject` to which tracking data will be published. This stream is also output directly by the node | 

###### Device input subjects
| Subject name      | Type          | Description                                                                                     |
|-------------------|---------------|-------------------------------------------------------------------------------------------------|
| **FrameEvents**   | `Harp.Timestamped<Aeon.Acquisition.VideoDataFrame>` | The `Subject` to subscribe to that carries frame events from a chosen camera | 

#### Usage
The trained model must first be exported to [Protocol buffer (.pb) format](https://protobuf.dev/) using the [`sleap-export`](https://sleap.ai/guides/cli.html#sleap-export) command line interface. 
Next, create a `GroupWorkflow` and give it an appropriate name, e.g. "PoseTracking". 
Inside, place a `PoseTracking (Aeon.Vision.Sleap)` node, externalise all properties, and connect it to the `WorkflowOutput`.

![poseTracking](../../workflows/poseTracking.svg)

## Logging
<!-- Seems to be copied over from PositionTracking - check  if correct. 
Also the workflow uses logdata, which also seems irrelevant -->
"TrackingEvents" from a `PoseTracking (Aeon.Vision.Sleap)` node can be logged along with the camera from which the "FrameEvents" originated using a [`LogHarpState (Aeon.Acquisition)`](target-node-logharpstate) node. 
First, add a `SubscribeSubject` to subscribe to the "TrackingEvents" `Subject` (e.g. "TrackingTop").
The events can then be formatted as `HarpMessages` and configured to write to register **200** (an unassigned register on all Harp devices) using the custom `FormatBinaryRegions (Aeon.Vision)` node.

![logTracking](../../workflows/logData.svg)

Multiple `PoseTracking` nodes can be used to track objects in different camera streams simultaneously. 
To do this, select a different "FrameEvents" `Subject` for each node and save the results to the corresponding camera folders.
<!-- To be coompleted 
## State persistence
Information on state recovery or persistence requirements, if applicable.

## Alerts
Explanation of any alert configurations and links to guides or further configuration steps.
-->
:::{seealso}
The [SLEAP](https://sleap.ai/) and [Bonsai.Sleap](https://bonsai-rx.org/sleap/index.html) documentation for more information on training models.
:::