(target-module-alerts)=
# Alerts

In order to capture as full a repertoire of natural behaviours as possible, the Aeon system is designed to monitor behaviour over extended periods in time of days, weeks or months, with no human disturbance to the animals. 
This presents unique challenges from a perspective of data acquisition and experimental control, since the system must be robust to, and ideally be able to recover from, system and hardware failures without constant human intervention. 
The Alerts module facilitates this using a system of webhooks and logs to record the state of the experiment, and to alert team members to hardware or system failures, as well as inconsistencies in data acquisition. 

## Nodes
(target-node-sendalert)=
### SendAlert
The node `SendAlert (Aeon.Acquisition)` accepts any string and sends it via an incoming webhook to post messages to a Microsoft Teams channel using an O365 connector. Full information on configuring these webhooks and generating a webhook url can be found in the [Microsoft documentation](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook?tabs=newteams%2Cdotnet).

:::{note}
O365 connectors will be deprecated in the coming months. This is a known [issue](aeon-experiments-github:issues/591) and an alternative will be developed and workflows updated on the public github repositories in time.
:::

#### Properties
| Property name      | Description                                                 |
|--------------------|-------------------------------------------------------------|
| **ConfigFile**     | The full or relative path of the configuration file         |

This configuration file is a simple text file that specifies the name of the system and the corresponding webhook URL. 
For example:

```
AEON: https://liveuclac.webhook.office.com/webhookb2/4a6da9d9-7456-4fe8-83a7-597dc94effa9@1faf88fe-a1234-5b6c-78d9-210a11d9a5c2/IncomingWebhook/523addf421e64fbcafadc1fc358c8ccf/ec5a3255-f2d6-47ca-ab3d-a81a0c34bc60
```

:::{important}
The system name in the configuration file must match the name of the computer, which can be set in Windows System Settings.
In Aeon, this file is stored in a "config" folder in the root of the repository. <!-- is this important? -->
::: 

#### Usage
<!-- Not immediately clear which is which, is  "EnvironmentAlertMessages" the `PublishSubject`? 
what is the EnvironmentAlerts subject?  
which one is the subscribed observer of `PublishSubject`? -->
<!-- What is "This" referring to? 
is `MultiCast` equivalent to `MultiCastSubject`? 
"this `Subject` presumably refers to the "EnvironmentAlerts" `Subject`? 
May be clearer if illustrated with a sample workflow? -->
Use a `PublishSubject` source node to publish and subscribe to the "EnvironmentAlerts" `Subject`. 
This can then be used anywhere in the workflow to send any custom alert, by using a `MultiCast` node to send formatted strings to this `Subject`. 

![SendAlertBase](../../workflows/EnvironmentAlertsBase.svg)

(target-node-formatlogmessage)=
### FormatLogMessage
All alert messages can also be logged to file, along with other lower priority 'notifications' that should be logged but is not urgent enough to warrant an alert. 
The `FormatLogMessage (Aeon.acquisition)` node formats the incoming data stream to enable the logging of alerts. 

#### Inputs
This node will accept any input but these must contain the information required for the alert message and timestamp. 
The members of the input used to configure the message are set in the [properties](target-node-formatlogmessage-properties).

#### Outputs
A sequence of `Harp.Timestamped<Aeon.acquisition.LogMessage>` with the following attributes. 

| Attribute name     | Type                             | Description                                                  |
|--------------------|----------------------------------|--------------------------------------------------------------|
| **Priority**       | `Aeon.Acquisition.PriorityLevel` | Specifies the priority level of the alert log.               |
| **Type**           | `string`                         | Specifies the type of alert under which this log is stored.  |
| **Message**        | `string`                         | Contains the actual message content to be logged.            |

(target-node-formatlogmessage-properties)=
#### Properties
| Property name        | Type            | Description                                                                                             |
|----------------------|-----------------|---------------------------------------------------------------------------------------------------------|
| **Format**           | `string`        | The composite format string used to specify the output message                                          |
| **Selector**         | `string`        | Specifies the inner properties from the input that will be included in the formatted log message        |
| **Priority**         | `enum`          | Sets the priority level of the log message, `Alert` or `Notification`                                   |
| **Type**             | `string`        | Defines the type of the log entry. Can be any `string` entry                                            |
| **Timestamp**        | `string`        | The inner property selected for use as the timestamp for each element in the sequence                   |

#### Usage
Prior to logging alerts, format the incoming message strings using a `FormatLogMessage (Aeon.acquisition)` node.
Once formatted, these timestamped messages can be `Multicast` to a shared "AlertLogs" `Subject`, allowing for the logging of both notifications and alerts.

![FormatLogMessage](../../workflows/formatLogMessage.svg)

The shared "AlertLogs" `Subject` is then provided as an input to the [`LogData (Aeon.Acquisition)`](target-node-logdata) node, which writes the log data to the specified file. 

![AlertLogs](../../workflows/alertLogs.svg)

(target-node-alertgate)=
### AlertGate
Many alerts may be triggered by events that occur at high frequency when in a faulty state. 
For example, if a device is desynchronised, then an alert will be generated every second until this condition is no longer true. 
In order to avoid unneccessary, repetitive alerts and overinflated alert logs, an `AlertGate (Aeon.acquisition)` node can be used to throttle specific alerts.

![AlertGate](../../workflows/alertGate.svg)

This node simply accepts any input stream, but only returns elements that arrive within the `AlertRefractoryPeriod`  property:

![AlertGate](../../workflows/alertGateDetail.svg)

Specific use cases for formatting and sending alerts are detailed in individual module references.