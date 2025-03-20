(target-module-monitors)=
# Device Synchronisation Monitors

All devices in the Aeon system are synchronised using a Harp [ClockSynchronizer](https://github.com/harp-tech/device.clocksynchronizer) device. 
Sychronisation is constantly monitored across devices using a combination of `HeartbeatMonitor (Aeon.Acquisition)` and `SynchronizerMonitor (Aeon.Acquisition)` nodes.

## Nodes
### HeartbeatMonitor
The `HeartbeatMonitor (Aeon.Acquisition)` node extracts the "heartbeats" from a specific Harp device.
"Heartbeats" are emitted by all Harp devices at 1Hz and should be synchronised.

#### Inputs
None

#### Outputs
A sequence of `Harp.Timestamped<string>`

#### Properties
This node takes no direct inputs but subscribes to and monitors the event stream `Subject` named in the node properties for heartbeat events every second (Harp register address 8 on all devices). 

| Property name      | Description                                                                         |
|--------------------|-------------------------------------------------------------------------------------|
| **Name**           | Set the name of the events `Subject` to monitor                                     |

#### Usage
##### Monitoring a single device
This example monitors the heartbeats from the ClockSynchronizer device itself.

:::workflow
![Aeon.Acquisition.HeartbeatMonitor](../../workflows/heartbeatMonitor.bonsai)
:::

##### Monitoring multiple devices
To monitor multiple devices at once, a `HeartbeatMonitor` node for each device should be added to a `GroupWorkflow` called, for example, "HeartbeatSources", and the results merged to the `WorkflowOutput` of the group.

:::workflow
![Aeon.Acquisition.HeartbeatSources merge](../../workflows/heartbeatSourcesInt.bonsai)
:::

(target-node-synchronizermonitor)=
### SynchronizerMonitor
The `SynchronizerMonitor (Aeon.Acquisition)` node is used to monitor the synchronisation status of acquisition devices, ensuring that all monitored devices are properly aligned and functioning in unison. 
It counts the number of devices in the ["HeartbeatSources" `GroupWorkflow`](#monitoring-multiple-devices) and compares heatbeats acquired from each device to the heartbeats of the ClockSynchronizer device. 

#### Inputs
Sequence of `Harp.Timestamped<string>`

#### Outputs
An observable sequence of custom `DynamicClass` with the following attributes. 

| Attribute name          | Type               | Description                                                      |
|-------------------------|--------------------|------------------------------------------------------------------|
| **MeanTimestamp**       | `double`           | The mean raw timestamp across all input streams                  |
| **MeanUtcTimestamp**    | `System.DateTime`  | The mean UTC timestamp across all input streams                  |
| **ExpectedDeviceCount** | `int`              | The number of synchronized input device streams                  |
| **DeviceCount**         | `long`             | The actual number of devices for which a heartbeat was received  |
| **MaxDifference**       | `double`           | The largest difference between timestamps from all devices       |
| **Elements**            | `string`           | The names of the input device streams                            |

#### Usage
Pass the output from the ["HeartbeatSources" `GroupWorkflow`](#monitoring-multiple-devices) to a `SynchronizerMonitor (Aeon.Acquisition)` node. 

:::workflow
![Aeon.Acquisition.HeartbeatSources](../../workflows/heartbeatSources.bonsai)
:::

## Alerts
Alerts can be set up using an `ExpressionCondition` node to define conditions under which an alert should be sent.
Conditions can be based on the [outputs from the `SynchronizerMonitor` node](#synchronizermonitor).
For example, alerts can be triggered if the number of expected devices does not match the number of devices sending heartbeats, or if one or more devices are sending desynchronised heartbeats.
The `ExpressionCondition` node then evaluates these conditions and passes the results to an [`AlertGate (Aeon.Acquisition)` node](target-node-alertgate), after which the alert is [sent](target-node-sendalert) and [logged to file](target-node-formatlogmessage).

:::workflow
![SynchMonitorLogs](../../workflows/synchMonitorLogs.bonsai)
:::