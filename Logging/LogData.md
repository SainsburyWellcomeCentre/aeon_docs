# **LogData**

The `LogData` node can save arbitrary data in a `.csv` file. Data are grouped into 1 hour long chunks for continuous logging and saved using the following naming convention:

```
"<logName>_<chunkTimestamp>.avi"`
```
For example: 
```
"Environment_BlockState_2024-06-27T10-00-00.csv"`
```
 It is generally the terminal node, with the typical pattern being to subscribe to a specific data stream subject, and pass directly to this node: 

![workflowImage](./Workflows/logData.svg)

Incoming datastreams can be combined into dynamic classes (using `Zip` or `CombineLatest` for example), and passed directly to the `LogData` node. In this case, the `Selector` property can be used to select specific members of the incoming data stream to save. These define column titles and order in the resulting .csv file.

### Inputs and Outputs:

**Inputs**
Any `Harp.TimeStamped<>` data stream whose member values can be written to .csv

**Outputs**
Returns inputs unchanged.
## **Properties of the node:**
| **Property Name**   | **Description**                                                                              |
|---------------------|----------------------------------------------------------------------------------------------------|
| **ClosingDuration** | *Description missing*                                                                              |
| **Heartbeats**      | The name of the subject carrying the `TimestampSeconds` events from the `ClockSynchronizer` that the system is synchronized with. |

### ***Misc:***

| **Property Name**   | **Description**                                                                                    |
|---------------------|----------------------------------------------------------------------------------------------------|
| **LogName**         | The name of this log. This will determine the naming of a dedicated folder and data files.         | 
| **Selector**        | Member selector property to select specific members of the incoming data stream.                   |