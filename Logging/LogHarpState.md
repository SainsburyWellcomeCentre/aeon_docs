# **LogHarpState**

The `LogHarpState` node logs all events from any individual harp device. Data are grouped into 1 hour long chunks for continuous logging and saved using the following naming convention:

```
"<DeviceName>_<registerAddress>_<chunkTimestamp>.bin"`
```
For example: 
```
"ClockSynchronizer_8_2024-06-27T10-00-00.bin"`
```

It is generally the terminal node, with the typical pattern being to subscribe to a specific harp device events subject, and pass directly to this node: 

![workflowImage](./Workflows/logHarpState.svg)

### Inputs and Outputs:

- **Inputs**:
Stream of `Harp.HarpMessages`, usually originating from a harp device.

- **Outputs**:
The `byte[]` array containing the contents of each harp message. This is generally not used downstream of this node. 
## **Properties of the node:**
### ***GroupClosing:***

| **Setting**         | **Description**                                                                                    |
|---------------------|----------------------------------------------------------------------------------------------------|
| **ClosingDuration** | *Description missing*                                                                              |
| **Heartbeats**      | The name of the subject carrying the `TimestampSeconds` events from the `ClockSynchronizer` that the system is synchronized with. |

### ***Misc:***

| **Setting** | **Description**                                                                                            |
|-------------|------------------------------------------------------------------------------------------------------------|
| **LogName** | The name of this log. This is usually the name of the harp device the harp stream originated from, and will determine the naming of dedicated folder and data files. |
