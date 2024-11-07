# Alerts

In order to capture as full a repertoire of natural behaviours as possible, the AEON system is designed to monitor behaviour over extended periods in time of days, weeks or months, with no human disturbance to the animals. This presents unique challenges from a perspective of data acquisition and experimental control, since the system must be robust to, and ideally able to recover from, system and hardware failures without constant human supervision. To facilitate this, we use a system of webhooks and logs to record the state of the experiment, and to alert team members to hardware or system failures, as well as inconsistencies in data acquisition. 

# Configure alerts and external connectors
## SendAlert node
The node `SendAlert (Aeon.Acquisition)` accepts any string and sends it via an incoming webhook to post messages to a Microsoft Teams channel using an O365 connector. Full information on configuring these webhooks and generating a webhook url can be found in the [Microsoft documentation](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook?tabs=newteams%2Cdotnet).

> ### ⚠️ Note
> O365 connectors will be deprecated in the coming months. This is a known [issue](https://github.com/SainsburyWellcomeCentre/ aeon_experiments/issues/591) and so an alternative will be developed and workflows updated on the public github repositories in time.

![SendAlertBase](./Workflows/EnvironmentAlertsBase.svg)

We use a `PublishSubject` source node to publish and subscribe to the 'EnvironmentAlerts' `Subject`. This can then be used anywhere in the workflow to send any custom alert, by using a `MultiCast` node to send formatted strings to this `Subject`. 

### **Properties of the node**

| **Property Name**  | **Description**                                             |
|--------------------|-------------------------------------------------------------|
| **ConfigFile**     | The full or relative path of the configuration file         |


This configuration file is a simple text file that specifies the name of the system and the corresponding webhook URL. 
For example:

```
AEON: https://liveuclac.webhook.office.com/webhookb2/4a6da9d9-7456-4fe8-83a7-597dc94effa9@1faf88fe-a1234-5b6c-78d9-210a11d9a5c2/IncomingWebhook/523addf421e64fbcafadc1fc358c8ccf/ec5a3255-f2d6-47ca-ab3d-a81a0c34bc60
```
In Project Aeon, this file is stored in a "config" folder in the root of the repository. The system name should match the name of the computer, which can be set in Windows System Settings.

# Configure alert Logs

We also keep a log of all alert messages in a dedicated log file, along with other, lower priority 'notifications' that should be logged but is not urgent enough to warrant an alert. 

![AlertLogs](./Workflows/alertLogs.svg)

In Project Aeon this is achieved by formatting a message string such that a [`logData`](../Logging/LogData.md) node will accept the inputs and log it to a data file. This is achieved using a [`FormatLogMessage (Aeon.acquisition)`](#formatlogmessage) node. These timestamped messages can then be `Multicast` to the shared "AlertLogs" `Subject` and used to log these timestamped notifications and alerts.

## FormatLogMessage
The `FormatLogMessage (Aeon.acquisition)` node formats the incoming datastream to allow [logging of alerts](#alert-logs) using the [`logData`](../Logging/LogData.md) node

![FormatLogMessage](./Workflows/formatLogMessage.svg)


### ***Inputs:***
This node will accept any input but these must contain the information required for the alert message and timestamp. The members of the input used to configure the message are set in the [properties](#properties-of-the-node-1).

### ***Outputs:***
Sequence of `Harp.Timestamped<Aeon.acquisition.LogMessage>` with the following attributes: 
| **Attribute** | **Type**                         | **Description**                                              |
|---------------|----------------------------------|--------------------------------------------------------------|
| **Priority**  | `Aeon.Acquisition.PriorityLevel` | Specifies the priority level of the alert log.               |
| **Type**      | `string`                         | Specifies the type of alert under which this log is stored.  |
| **Message**   | `string`                         | Contains the actual message content to be logged.            |

### **Properties of the node:**
| **Property Name**    | **Type**        | **Description**                                                                                         |
|----------------------|-----------------|---------------------------------------------------------------------------------------------------------|
| **Format**           | `string`        | The composite format string used to specify the output message                                          |
| **Selector**         | `string`        | Specifies the inner properties from the input that will be included in the formatted log message        |
| **Priority**         | `enum`          | Sets the priority level of the log message, `Alert` or `Notification`                              |
| **Type**             | `string`        | Defines the type of the log entry. Can be any `string` entry                                                  |
| **Timestamp**        | `string`        | The inner property selected for use as the timestamp for each element in the sequence                   |

# AlertGate
Many alerts may be triggered by events that occur at high frequency when in a fault state. For example, if a device is desynchronised, then an alert will be generated every second until this condition is no longer true. In order to avoid unneccessary, repetitive alerts and overinflated alert logs, we use an `AlertGate (Aeon.acquisition)` node to throttle specific alerts.

![AlertGate](./Workflows/alertGate.svg)

This node simply accepts any input stream, but only returns elements that arrive within the `AlertRefractoryPeriod`  property:

![AlertGate](./Workflows/alertGateDetail.svg)

 Specific use cases for formatting and sending alerts is detailed in [individual module](../HardwareDevices/) documentation

# Subject Alerts
TBC