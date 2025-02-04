(target-module-logging)=
# Logging
The logging module facilitates the recording of various types of data streams during experiments. 
These nodes enable the continuous logging of data into structured formats, ensuring that all relevant information is captured and stored for subsequent analysis.
Data is grouped into 1-hour long chunks for efficient logging and retrieval.

## Nodes
(target-node-logdata)=
### LogData 
The `LogData (Aeon.Acquisition)` node saves arbitrary data to a `.csv` file. 
Data is saved in hourly chunks using the following naming convention: 
```
<logName>_<chunkTimestamp>.csv
```
For example: 
```
Environment_BlockState_2024-06-27T10-00-00.csv
```

#### Inputs
Any `Harp.TimeStamped<>` data stream whose member values can be written to a `.csv` file.

#### Outputs
Inputs are returned unchanged. 

#### Properties
##### General
| Property name | Description                                               |
|---------------|-----------------------------------------------------------|
| **ClosingDuration** |  Time delay, in seconds to ensure complete closure of consecutive files |                                                                           
| **Heartbeats**      | The name of the subject carrying the `TimestampSeconds` events from the `ClockSynchronizer` that the system is synchronised with |

##### Miscellaneous
| Property name | Description                                   |
|---------------|-----------------------------------------------|
| **LogName**   | The name of this log. This will determine the naming of a dedicated folder and data files | 
| **Selector**  | Member selector property to select specific members of the incoming data stream           |

#### Usage
The `LogData (Aeon.Acquisition)` node is generally the terminal node, to which a `SubscribeSubject` passes the data stream it is subscribed to for logging. 

:::workflow
![Aeon.Acquisition.LogData](../../workflows/logData.bonsai)
:::

Incoming data streams can also be combined into dynamic classes using operators like `Zip` or `CombineLatest`. 
These combined streams can then be passed directly to a `LogData (Aeon.Acquisition)` node. 
The `Selector` property can be used to specify which members of the incoming data stream to be included for defining the column names and order in the resulting `.csv` log file.

(target-node-logharpstate)=
### LogHarpState 
The `LogHarpState (Aeon.Acquisition)` node logs all events from any individual Harp device. 
Data is saved in hourly chunks using the following naming convention: 
```
<DeviceName>_<registerAddress>_<chunkTimestamp>.bin
```
For example: 
```
ClockSynchronizer_8_2024-06-27T10-00-00.bin
```

#### Inputs
Stream of `Harp.HarpMessages`, usually originating from a Harp device.

#### Outputs
The `byte[]` array containing the contents of each Harp message. 
This is generally not passed to any operators downstream of this node.

#### Properties
##### GroupClosing
| Property name | Description                                               |
|---------------|-----------------------------------------------------------|
| **ClosingDuration** |  Time delay, in seconds, to ensure complete closure of consecutive files  |                                                                           
| **Heartbeats**      | The name of the subject carrying the `TimestampSeconds` events from the `ClockSynchronizer` that the system is synchronised with |

##### Miscellaneous
| Property name | Description                                   |
|---------------|-----------------------------------------------|
| **LogName**   | The name of this log. This is usually the name of the Harp device the Harp stream originated from, and will determine the naming of dedicated folder and data files |

#### Usage
The `LogHarpState (Aeon.Acquisition)` node is generally the terminal node, to which a `SubscribeSubject` passes the Harp device events `Subject` it is subscribed to for logging.

:::workflow
![Aeon.Acquisition.LogHarpState](../../workflows/logHarpState.bonsai)
:::

(target-node-logvideo)=
### LogVideo 
The `LogVideo (Aeon.Video)` node saves two files.
The first file contains Harp timestamped video frames stored in `.avi` format.
The second file is a `.csv` file that stores the corresponding unique index ID and timestamp for each frame stored in the `.avi` file.
Data is saved in hourly chunks using the following naming convention: 
```
<CameraStreamName>_<chunkTimestamp>.<ext>
```
For example: 
```
"CameraTop_2024-06-27T10-00-00.avi"
"CameraTop_2024-06-27T10-00-00.csv"
```

#### Inputs
Stream of `Harp.Timestamped<Aeon.Video.VideoDataFrame>`, originating from a [`SpinnakerVideoSource (Aeon.Video)`](target-node-spinnakervideosource) node.

#### Outputs
Stream of raw video images of type `OpenCV.Net.IPlImage`. 

#### Properties
##### GroupClosing
| Property name | Description                                               |
|---------------|-----------------------------------------------------------|
| **ClosingDuration** |  Time delay, in seconds, to ensure complete closure of consecutive files |                                                                           

##### Miscellaneous
| Property name | Description                                   |
|---------------|-----------------------------------------------|
| **LogName**   | The name of this log. This will determine the naming of a dedicated folder and data files | 

#### Usage
The `LogVideo (Aeon.Video)` node is generally the terminal node, to which a `SubscribeSubject` passes the frame events `Subject` it is subscribed to for logging.

:::workflow
![Aeon.Video.LogVideo](../../workflows/logVideo.bonsai)
:::