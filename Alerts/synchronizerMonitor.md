# Monitoring Synchronized Devices

All devices in an Aeon system are synchronised using a harp [ClockSynchronizer](https://github.com/harp-tech/device.clocksynchronizer) device. Sychronization is constantly monitored across devices using a combination of `HeartbeatMonitor (Aeon.acquisition)` and `SynchronizerMonitor (Aeon.acquisition)` nodes.

## HeartbeatMonitor (Aeon.acquisition)
![Aeon.Acquisition.HeartbeatMonitor](./Workflows/heartbeatMonitor.svg)

### **Input and Outputs:**

#### ***Inputs:***
None

#### ***Outputs***
An observable sequence of `Harp.Timestamped<string>` 

### ***Properties of the node:***
This node takes no direct inputs but subscribes to and monitors the event stream `Subject` named in the node properties for heartbeat events every second (harp register address 8 on all devices). In this example, we are monitoring the heartbeats from the ClockSynchronizer device itself.

| **Property Name**  | **Description**                                                                           |
|--------------------|-------------------------------------------------------------------------------------------|
| **Name**           | Set the name of the events `Subject` to monitor                                           |

### Monitoring multiple devices:
In order to monitor multiple devices at once, a `HeartbeatMonitor` node for each device should be added to a `GroupWorkflow` called, for example, 'HeartbeatSources', and the results merged to the `WorkflowOutput` of the group.

![Aeon.Acquisition.HeartbeatSources merge](./Workflows/heartbeatSourcesInt.svg)


## SynchronizerMonitor (Aeon.acquisition)

The output from this node can then be passed to a `SynchronizerMonitor (Aeon.aquisition)` node. This node counts the number of devices in your "HeartbeatSources" `GroupWorkflow` and compares heatbeats acquired from each device to the heartbeats of the clock synchroniser device. 

![Aeon.Acquisition.HeartbeatSources](./Workflows/heartbeatSources.svg)

### **Input and Outputs:**

#### ***Inputs:***
Sequence of `Harp.Timestamped<string>`

#### ***Outputs***
An observable sequence of custom `DynamicClass` with the following attributes. 

| **Name**                | **Type**           |**Description**                                                   |
|-------------------------|--------------------|------------------------------------------------------------------|
| **MeanTimestamp**       | `double`           | The mean raw timestamp across all input streams                  |
| **MeanUtcTimestamp**    | `System.DateTime`  | The mean UTC timestamp across all input streams                  |
| **ExpectedDeviceCount** | `int`              | The number of synchronized input device streams                  |
| **DeviceCount**         | `long`             | The actual number of devices for which a heartbeat was received  |
| **MaxDifference**       | `double`           | The largest difference between timestamps from all devices       |
| **Elements**            | `string`           | The names of the input device streams                            |

## Conditioning and sending alerts

We then use an `ExpressionCondition` node to define conditions under which an alert should be sent, given the above values. For example if the number of expected devices does not match the number of devices sending heartbeats, or if one or more devices are sending de-synchronised heartbeats. 

This is then passed to an [`AlertGate (Aeon.acquisition)`](Alerts.md#alertgate) node before being split and formatted for [`EnvironmentAlerts`](Alerts.md#alerts) and [`AlertLogs`](Alerts.md#alert-logs)

![SynchMonitorLogs](./Workflows/synchMonitorLogs.svg)